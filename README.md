# Blooket-Icons
A JSON file with all of the blooket icon links from the Blooket Amazon AWS servers. Don't ask how long it took to compile this.
## Updating
Hopefully this should be updated with the latest blooks, however, if not, please don't hesitate to [leave an issue](https://github.com/SorkoPiko/Blooket-Icons/issues/new) and I'll sort it out as soon as possible.
## Invalid Link
I typed all of these in manually, so if any of the links don't work, please ask me to fix it immediately by [leaving an issue](https://github.com/SorkoPiko/Blooket-Icons/issues/new).
## How do I use these?
Just import the `icons.min.json` into your script and you can then find the link of any Blook by indexing the dictionary with the Blook's technical name (e.g. [Rainbow Astronaut](https://blooket.s3.us-east-2.amazonaws.com/blooks/bonus/mysticals/rainbowAstronaut.svg) would become `rainbowAstronaut`).
However, if you want to be able to use it with the Blook name returned by the Blooket API, I recently added a `blooketApi` folder, which does just that.