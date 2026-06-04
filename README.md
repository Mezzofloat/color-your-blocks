This is meant to be a recreation of the Colour Your World challenge seen [here](https://www.youtube.com/watch?v=1hVX08jWaHE), by TheMobCave. I created this because the challenge is a set of resource packs. Each texture is assigned one color and converted to a solid texture of that color, which doesn't look great when all put together. Another minor reason I did this is that the latest version it supports is 1.11, and I wanted to somewhat modernize it. Unfortunately, Minecraft doesn't natively support textures that add onto each other, so this is my attempt to circumvent that.

# Usage:

In the terminal, enter "python mergeresourcepack.py -c {color}" where color is one of the 16 minecraft colors in lowercase with dashes for spaces (red, lime, light-blue, etc). Then the pack in color-your-blocks will be updated with the color you specified.

Alternatively, if you enter "python mergeresourcepack.py --restart", then color-your-blocks will be reset back to white.

## Goals:

* When every color is unlocked, it should be indistinguishable from vanilla Minecraft textures.
* You can easily unlock a color/texture pack when you need to.
    * Ideally, this should be a mod that automatically unlocks each color when you complete the requirements, but that's outside my experience!
* The challenge should be a fun experience overall (not really a priority yet).

## Folders

* color-your-blocks: the resource pack that will ultimately be used by the player
* full: all 1.21.10 textures
* full_subset: the 1.21.10 textures that the resource pack pulls from
* masks: the discretized textures that determines what pixel is what color
* white: the starting texture pack, used when restarting the pack