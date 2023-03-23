# Tweet Generator ![Built with Python](https://img.shields.io/badge/python-v3.7-yellow)

Generate Phrases with ChatGPT3 and then scrapes twitter to send the phrase


- Phrase Generator
  1. Generate Phrase
  2. Push the phrases in a queue (AWS SQS)
  
- Tweet Servce
  1. Polls the Phrases from the queue
  2. Sent a tweet with the phrase
