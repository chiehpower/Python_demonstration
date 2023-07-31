'''
Use the base model. Take almost ~2GB GPU memory.
'''

import whisper
import time
import os 

input_file = 'wav/en-US_sample.wav'
model = whisper.load_model("base")
result = model.transcribe(input_file)
print(result)
'''
{'text': ' What is natural language processing?', 
'segments': [{'id': 0, 'seek': 0, 'start': 0.0, 'end': 5.0, 
'text': ' What is natural language processing?', 
'tokens': [50364, 708, 307, 3303, 2856, 9007, 30, 50614], 
'temperature': 0.0, 
'avg_logprob': -0.43793416023254395, 
'compression_ratio': 0.8181818181818182, 
'no_speech_prob': 0.04243078455328941}], 
'language': 'en'}
'''
print(result["text"])

'''
$ python3 whisper_test.py                                                                                                                                         
NumbaDeprecationWarning: The 'nopython' keyword argument was not supplied to the 'numba.jit' decorator. 
The implicit default value for this argument is currently False, 
but it will be changed to True in Numba 0.59.0. 
See https://numba.readthedocs.io/en/stable/reference/deprecation.html#deprecation-of-object-mode-fall-back-behaviour-when-using-jit for details.
  def backtrace(trace: np.ndarray):
100%|███████████████████████████████████████| 139M/139M [00:26<00:00, 5.40MiB/s]
What is natural language processing?
'''

# model = whisper.load_model("base")
folder = 'wav'
all_files = os.listdir(folder)
for i in all_files:
    if i.split('.')[-1] != 'wav' and i.split('.')[-1] != 'ogg':
        continue
    print(f"\nThe file is {i}")
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(os.path.join(folder, i))
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    st = time.time()
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(result.text)
    print(f"Inference time: {time.time() - st}")


'''
The file is es-US_sample.wav
Detected language: es
Existe mutaciones que alteran los pigmentos de color basados en carotenotes, pero son raras.

The file is zh-CN_sample.wav
Detected language: zh
应该做自己想做的事

The file is pt-BR_sample.wav
Detected language: pt
Como poderia ser estranho?

The file is headroom-sample.ogg
Detected language: en
AI is powering change in every industry, from speech recognition and recommenders to medical imaging and improved supply chain management. AI is providing enterprises the compute power, tools and algorithms their teams need to do their life's work.

The file is en-US_sample.ogg
Detected language: en
What is natural language processing?

The file is fr-FR_sample.wav
Detected language: fr
des arbres ont été plantés

The file is ar-AR_sample.wav
Detected language: ar
هل بإمكانك أنطاطين المزيدة من القواة من فضل؟

The file is en-GB_sample.wav
Detected language: en
The tea was a little bit too hot.

The file is de-DE_sample.wav
Detected language: de
Nammensgebend für den deutschen Begriff ist, das weitlich schlaffende auf diese Region liegen.

The file is hi-IN_sample.wav
Detected language: hi
v1 7 kild rai hai

The file is ru-RU_sample.wav
Detected language: ru
Египет проголосовал за проехрезолюции, полностью сознавая два слабых положения, которые он содержит.

The file is es-ES_sample.wav
Detected language: es
El río Tigris tenía un tipo de agua agreguzuz.

The file is ja-JP_sample.wav
Detected language: ja
運動のため隣の駅まで歩きます。

The file is en-US_sample.wav
Detected language: en
What is natural language processing?

The file is it-IT_sample.wav
Detected language: it
Da la sozione congiunta le sedi stanno beneficiando scambi culturali e personali.

The file is en-US_wordboosting_sample.wav
Detected language: en
Antibata and Abluper both transformable based language models are examples of the emerging work in using graph neural networks to design protein sequences for particular target antigens.
'''