import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    cowsay.dragon("Hello, " + sys.argv[1])
    cowsay.ghostbusters("Hello, " + sys.argv[1])
    cowsay.kitty("Hello, " + sys.argv[1])
    cowsay.stegosaurus("Hello, " + sys.argv[1])
    cowsay.trex("Hello, " + sys.argv[1])
    cowsay.turtle("Hello, " + sys.argv[1])
    cowsay.tux("Hello, " + sys.argv[1])
else:
    print("Thanks for using cowsay!")