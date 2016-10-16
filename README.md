# kotoha-slack
A slack command integration for [kotoha](https://github.com/konifar/kotoha), a great chrome extension to find Anime quotes!

![demo](https://github.com/tomoima525/kotoha-slack/blob/master/img/demo.gif)

# How it works
From any channel, just type:
```
/kotoha keyword [search term]
```

Or if you want to search from a title of Animes:
```
/kotoha tag [search term]
```

Currently, most of quotes are in Japanese, but you are welcomed to add a new one using [kotoha](https://github.com/konifar/kotoha) extension from Chrome.

# Integrate to your Slack

1. Go to your channel and select **Customize Slack**
2. From the side menu, select **Configure apps**
3. Select **Custom Integrations** and you will see **Slash Commands** on the list
4. Click on **Add Configuration** and input information below  
![img_3](https://github.com/tomoima525/kotoha-slack/blob/master/img/img_3.png)
5. You are ready to go!

# Developing kotoha-slack
This command is written in python and runs on herokuapp.

After clone the project, install required libraries:
```
$ pip install -r requirements.txt
```
then, run with DEBUG mode
```
$ DEBUG=True python app.py
```

# Acknowledgement
Many Thanks to konifar[twitter](https://twitter.com/konifar)[github](https://github.com/konifar) for letting me use the api of kotoha :)

# License
MIT License.
Copyright (c) 2016 Tomoaki Imai

# Contributing

- Please use the [issue tracker](https://github.com/tomoima525/kotoha-slack/issues) to report any bugs and feature requests or let me know from twitter [@tomoima525](https://twitter.com/tomoima525)
