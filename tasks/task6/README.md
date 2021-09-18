## Problem 2
I need to create a scheduler that allows me to send/receive messages in a specific time 
- the scheduler should let me set a time:
    - using hour, minutos and seconds 
    - using periods of time, like every hour
- a list of platforms can be configured to send the message. 
- after the message is sent to the first platform, a response should be received in the next 10 minutes, if no response is received the message will be sent to the next platform and wait for the response again and so on. 
- Platforms example: mail, skype, slack, discord.

## Problem 3
In an ice-cream company that makes ice cream based on client(company) preferences:
- the flavor of the ice cream 
- choose the ingredients
- pasteurization level
- Homogenization level
- creaming level

after that the product is delivered, in each stage the ice cream should be validated, if the product doesnt meet the levels needed, the product should be discarded.