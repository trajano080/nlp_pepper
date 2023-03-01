# NLP for Pepper Robot
This system allows a Pepper robot to listen to speech and understand it to either carry out orders or answer questions. 

It does this by first detecting when someone is speaking to it. It must be able to do this even when there is some background noise, so we have done some tests to verify that it works correctly. It then records the sound and saves it, filtering out background noise. After that, the speech is turned into text. Finally, parses the text and deduces its meaning.


Note: This code was developed for a closed source project. I have only obtained permission to re-upload and show the code I worked on, not the rest of the project.
