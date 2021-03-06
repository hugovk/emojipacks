# emojipacks

[![Build Status](https://travis-ci.org/hugovk/emojipacks.svg?branch=master)](https://travis-ci.org/hugovk/emojipacks)

> CLI to bulk upload emojis to your Slack!

## Install

*Note you must have `node` and `npm` installed. If you don't, go to [nodejs.org](https://www.nodejs.org) and follow the install instructions there.*

```bash
$ npm install -g emojipacks
```

or

```bash
$ git clone git@github.com:hugovk/emojipacks.git
$ cd emojipacks
$ make
```

## Usage

There is only one command:

```bash
$ emojipacks
```

It'll ask you a few questions:

```bash
Slack subdomain: 20percentclub
Email address login: andyjiang@gmail.com
Password: *********
Path or URL of Emoji yaml file: ./packs/futurama.yaml
```

Or you can create a credentials file in your home directory: `~/.emojipacks.yaml`:

```yaml
subdomain: 20percentclub
email: andyjiang@gmail.com
```

_Note that for security it will always ask for your password_

Then, let it work its magic:

```bash
Starting import
Got tokens
Logged in
Upload crumb is s-1437797544-90b75206a7-☃
Getting emoji page
Uploading bender with http://i.imgur.com/7zYM751.png
Uploading amywong with http://i.imgur.com/DgKkcCi.png
 .
 .
 .
Uploading hypnotoad with http://i.imgur.com/o7tyjxN.gif
Uploaded emojis
```

Note that the emoji pack to upload can be a **path** to a yaml file on your machine or a **URL**, like [http://www.emojipacks.com/packs/food.yaml](http://www.emojipacks.com/packs/food.yaml).

## Emoji Yaml File

Also note that the yaml file must be indented properly and formatted as such:

```yaml
title: food
emojis:
  - name: apple
    src: http://i.imgur.com/Rw0Vlda.png
  - name: applepie
    src: http://i.imgur.com/g4RU1fM.png
```

..with the `src` pointing to an image file. According to Slack:

- Square images work best
- Image can't be larger than 128px in width or height
- Image must be smaller than 64K in file size

It is also possible to give multiple names to a single emoji using yaml such as:
```yaml
title: octicons
emojis:
  - name: pr
    aliases:
      - pullrequest
      - mergerequest
    src: https://i.imgur.com/rhwNxfc.png
```


## Emoji packs

- [futurama](http://www.emojipacks.com/packs/futurama.yaml)
- [food](http://www.emojipacks.com/packs/food.yaml)
- [skype](http://www.emojipacks.com/packs/skype.yaml)
- [starwars](http://www.emojipacks.com/packs/starwars.yaml)
- [startups](http://www.emojipacks.com/packs/startups.yaml)
- [businessfish](http://www.emojipacks.com/packs/businessfish.yaml)
- [hipchat](https://raw.githubusercontent.com/hugovk/emojipacks/master/packs/hipchat.yaml)
- [twitch](https://raw.githubusercontent.com/hugovk/emojipacks/master/packs/twitch.yaml)
- [Slackmojis](https://raw.githubusercontent.com/hugovk/emojipacks/master/packs/slackmojis.yaml)
- [parrotparty](https://raw.githubusercontent.com/hugovk/emojipacks/master/packs/parrotparty.yaml) ([Parrot](http://cultofthepartyparrot.com/) [Paint](http://cultofthepartyparrot.com/paint/))
- [Finland](https://raw.githubusercontent.com/hugovk/emojipacks/master/packs/finland.yaml)
- [pokemongo: items](https://raw.githubusercontent.com/hugovk/emojipacks/master/packs/pokemongo.yaml)
- [Pokémon Go: Pokémon](https://raw.githubusercontent.com/Templarian/slack-emoji-pokemon/master/pokemon.yaml) ([Prefixed `pokemon-*`](https://raw.githubusercontent.com/Templarian/slack-emoji-pokemon/master/pokemon-prefix.yaml))
- [nekoatsume](https://raw.githubusercontent.com/hugovk/emojipacks/master/packs/nekoatsume.yaml)
- [octicons](https://raw.githubusercontent.com/hugovk/emojipacks/master/packs/octicons.yaml)
- [pokemon](https://raw.githubusercontent.com/jaylynch/pokemoji/master/pokemon-by-name.yaml)
- [devicon](https://raw.githubusercontent.com/izumin5210/emojipack-for-devicon/master/png/devicon.yaml) ([Devicon](http://devicon.fr/))

![](http://media1.giphy.com/media/68H7QjnqFOn2E/100.gif)

Want to contribute? [Suggest an emoji pack](https://20p.typeform.com/to/xOFDyq)!

## Batch use

You can set the following environment variables instead of being prompted interactively for the parameters:

* `SLACK_SUBDOMAIN`
* `SLACK_EMAIL`
* `SLACK_PASSWORD`
* `SLACK_EMOJIPACK`

For example:

    SLACK_SUBDOMAIN=example SLACK_EMAIL=foobar@example.com SLACK_PASSWORD='secret-pw' SLACK_EMOJIPACK=packs/futurama.pack bin/emojipacks

This is convenient when you want to import many emoji packs at once, you might use this to import ![:allthethings:](https://dujrsrsgsd3nh.cloudfront.net/img/emoticons/allthethings-1414024836@2x.png) at once for example:

    export SLACK_SUBDOMAIN=example SLACK_EMAIL=foobar@example.com SLACK_PASSWORD='secret-pw'
    for emoji in packs/*.yaml; do  SLACK_EMOJIPACK="$emoji" bin/emojipacks; done

Please be cautious and know that if you use the environment variable configurations to drive the import on a multiuser system, that other people logged in could observe your Slack domain, email, and password while the script is running, as environment variables are not private. This does not matter so much on a single user system, such as your personal computer.

## Troubleshooting

This script will essentially log into your Slack and then submit a `POST` request on the emoji upload form page. If you are seeing errors, make sure that:
- **you have Slack privileges to add custom emojis**: otherwise, the script won't be able to get to the emoji upload form
- **you disabled two-factor authentication**: again, having two-factor enabled will prevent the script from getting to the necessary emoji upload form
- **your credentials are correct**: if you have done all of the following correctly try running the command **emojipacks -d**

*Still having issues? Create an issue [here](https://github.com/lambtron/emojipacks/issues/new).*

*Enjoyed this project? Check out my [blog](http://blog.andyjiang.com) for more*.

## License (MIT)

```
WWWWWW||WWWWWW
 W W W||W W W
      ||
    ( OO )__________
     /  |           \
    /o o|    MIT     \
    \___/||_||__||_|| *
         || ||  || ||
        _||_|| _||_||
       (__|__|(__|__|
```

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

