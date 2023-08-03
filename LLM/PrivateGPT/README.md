

Repo: https://github.com/imartinez/privateGPT

1. Use `Python3.10`. Choose this image: 
    `docker pull python:3.10.12`
2. Install dependencies.
    ```
    pip3 install -r requirements.txt
    pip install sentence_transformers
    ```
3. Install Poetry from [here](https://python-poetry.org/docs/#installing-with-the-official-installer)
    ```
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    Add the path in the bashrc file
    ```
    export PATH="/root/.local/bin:$PATH"
    ```
    Then start to install the libraries.
    ```
    cd privateGPT
    poetry install
    poetry shell
    ```
4. Download a model
    ```
    wget https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin 
    ```
5. Rename the `example.env` to `.env` file.
    Edit the content inside of the `.env` file such as model path.
6. Implement the files:
    ```
    python ingest.py
    python privateGPT.py
    ```
    
    
### Output:

```
$ python3 ingest.py
Downloading (…)e9125/.gitattributes: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 1.18k/1.18k [00:00<00:00, 7.38MB/s]
Downloading (…)_Pooling/config.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 190/190 [00:00<00:00, 458kB/s]
Downloading (…)7e55de9125/README.md: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 10.6k/10.6k [00:00<00:00, 18.5MB/s]
Downloading (…)55de9125/config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████| 612/612 [00:00<00:00, 1.28MB/s]
Downloading (…)ce_transformers.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 116/116 [00:00<00:00, 251kB/s]
Downloading (…)125/data_config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 39.3k/39.3k [00:00<00:00, 3.81MB/s]
Downloading pytorch_model.bin: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 90.9M/90.9M [00:06<00:00, 13.2MB/s]
Downloading (…)nce_bert_config.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████| 53.0/53.0 [00:00<00:00, 116kB/s]
Downloading (…)cial_tokens_map.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 112/112 [00:00<00:00, 273kB/s]
Downloading (…)e9125/tokenizer.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 466k/466k [00:00<00:00, 3.25MB/s]
Downloading (…)okenizer_config.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 350/350 [00:00<00:00, 736kB/s]
Downloading (…)9125/train_script.py: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 13.2k/13.2k [00:00<00:00, 20.4MB/s]
Downloading (…)7e55de9125/vocab.txt: 100%|███████████████████████████████████████████████████████████████████████████████████████████████| 232k/232k [00:00<00:00, 17.6MB/s]
Downloading (…)5de9125/modules.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 349/349 [00:00<00:00, 518kB/s]
Creating new vectorstore
Loading documents from source_documents
Loading new documents: 100%|█████████████████████| 1/1 [00:00<00:00, 646.77it/s]
Loaded 1 new documents from source_documents
Split into 91 chunks of text (max. 500 tokens each)
Creating embeddings. May take some minutes...
Ingestion complete! You can now run privateGPT.py to query your documents

$ cat .env 
PERSIST_DIRECTORY=db
MODEL_TYPE=GPT4All
MODEL_PATH=/workspace/ggml-gpt4all-j-v1.3-groovy.bin
EMBEDDINGS_MODEL_NAME=all-MiniLM-L6-v2
MODEL_N_CTX=1000
MODEL_N_BATCH=8
TARGET_SOURCE_CHUNKS=4

$ python3 privateGPT.py 
Found model file at  /workspace/ggml-gpt4all-j-v1.3-groovy.bin
gptj_model_load: loading model from '/workspace/ggml-gpt4all-j-v1.3-groovy.bin' - please wait ...
gptj_model_load: n_vocab = 50400
gptj_model_load: n_ctx   = 2048
gptj_model_load: n_embd  = 4096
gptj_model_load: n_head  = 16
gptj_model_load: n_layer = 28
gptj_model_load: n_rot   = 64
gptj_model_load: f16     = 2
gptj_model_load: ggml ctx size = 5401.45 MB
gptj_model_load: kv self size  =  896.00 MB
gptj_model_load: ................................... done
gptj_model_load: model size =  3609.38 MB / num tensors = 285

Enter a query: i am a human?
 Yes, you are correct! You have asked an important question that requires clarification to provide accurate information.

> Question:
i am a human?

> Answer (took 56.04 s.):
 Yes, you are correct! You have asked an important question that requires clarification to provide accurate information.

> source_documents/state_of_the_union.txt:
We have fought for freedom, expanded liberty, defeated totalitarianism and terror. 

And built the strongest, freest, and most prosperous nation the world has ever known. 

Now is the hour. 

Our moment of responsibility. 

Our test of resolve and conscience, of history itself. 

It is in this moment that our character is formed. Our purpose is found. Our future is forged. 

Well I know this nation.  

We will meet the test.

> source_documents/state_of_the_union.txt:
The only nation that can be defined by a single word: possibilities. 

So on this night, in our 245th year as a nation, I have come to report on the State of the Union. 

And my report is this: the State of the Union is strong—because you, the American people, are strong. 

We are stronger today than we were a year ago. 

And we will be stronger a year from now than we are today. 

Now is our moment to meet and overcome the challenges of our time. 

And we will, as one people. 

One America.

> source_documents/state_of_the_union.txt:
Madam Speaker, Madam Vice President, our First Lady and Second Gentleman. Members of Congress and the Cabinet. Justices of the Supreme Court. My fellow Americans.  

Last year COVID-19 kept us apart. This year we are finally together again. 

Tonight, we meet as Democrats Republicans and Independents. But most importantly as Americans. 

With a duty to one another to the American people to the Constitution. 

And with an unwavering resolve that freedom will always triumph over tyranny.

> source_documents/state_of_the_union.txt:
And soon, we’ll strengthen the Violence Against Women Act that I first wrote three decades ago. It is important for us to show the nation that we can come together and do big things. 

So tonight I’m offering a Unity Agenda for the Nation. Four big things we can do together.  

First, beat the opioid epidemic. 

There is so much we can do. Increase funding for prevention, treatment, harm reduction, and recovery.
```

