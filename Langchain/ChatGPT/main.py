from langchain import OpenAI
from langchain.callbacks import get_openai_callback
# from langchain.callbacks.base import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os
from langchain.callbacks.manager import AsyncCallbackManager
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(
    temperature=0,
	openai_api_key=os.environ["OPENAI_API_KEY"],
	model_name="text-davinci-003",
    callback_manager=AsyncCallbackManager([StreamingStdOutCallbackHandler()]),
    verbose=True,
    streaming=True
)

response = llm("Please write an English poem with 50 lines and 10 syllables per line.")

"""
The sun is shining bright,
A new day is in sight,
The birds are singing sweet,
A gentle breeze on my feet.

The sky is so blue,
The clouds are so few,
The trees are so tall,
The flowers so small.

The grass is so green,
The air is so clean,
The lake is so still,
The mountains so high on the hill.

The sky is so vast,
The stars are so bright,
The moon is so full,
The night is so still.

The sun is so warm,
The clouds are so white,
The wind is so gentle,
The rain is so light.

The birds are so chirpy,
The trees are so leafy,
The flowers are so fragrant,
The sky is so pleasant.

The sun is so bright,
The moon is so round,
The stars are so twinkling,
The night is so sound.

The day is so long,
The night is so short,
The sun is so hot,
The moon is so cold.

The birds are so cheerful,
The trees are so tall,%  
"""