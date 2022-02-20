# Overview

This is a simple code to convert english characters into dwarvish. It takes in user input, pulls form a cloud database

This code pulls from a cloud database, and uses the dictionary stored there to translate english characters into Dwarvish/Cirth characters.

The main purpose of this was to learn how to work with CLoud databases, Specifically Google Firebase. 

Below is my Code Demo Video where I walk through my code.

[Software Demo Video](https://youtu.be/Axc70mWDnMY)

# Cloud Database

I'm Using Google Firebase

THis program uses one collection called "Letters" that conntains a series of documents named after the different english letters/ or letter combinations that translate to a specific symbol. Each Document consists of a field, the name of the language, and the symbol(Pulled from unicode most likely).

# Development Environment

VS Code and Google Firebase

This was all done in Python 3

# Useful Websites

* [Stack Overflow](https://stackoverflow.com/)
* [YouTube](http://youtube.com)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* I want to figure out how to fix the issue where unicode key is inputed by user and not actually translated to the unicode symbole. It stayes and the raw 6 symbol key used to find the desired symbol in the database.
* It would be fun to make it look prettier.
* If it was possible to find the actual characters that dont exist in the unicode library, that would be cool but it's probbaly a low probability of that happening.