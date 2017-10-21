https://api.slack.com/incoming-webhooks
... this link contains 1) send timely messaged 2) message in a rich format [ although not by our bot. 
by the integrated incoming-webhook-bot of slack]

https://api.slack.com/rtm
... one that we're using

**You cannot provide attachments nor buttons to messages posted over the RTM API.
If your bot user needs to send more complex messages, use the web API's chat.postMessage or chat.postEphemeral.**
