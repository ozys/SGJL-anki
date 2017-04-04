# SGJL 01 - Remembering the Hiragana

### Course notes:

In obtaining literacy in the Japanese language, Romaji (Roman Characters aka the alphabet) are the devil. Only in these two courses (Hiragana and Katakana) are romaji are used. Beyond this, you are expected to only use kana when learning new grammar or vocabulary words. Romaji will not be used beyond this point. In addition, this course is **NOT** about learning new words. Don't worry about learning what the words mean; instead, the course uses authentic Japanese words as example pronunciations to reinforce understanding both spoken and written kana. The test lessons should therefore go much, much quicker as each example word will **ONLY** use kana that was previously learned in the lessons.

Each kana course will have six YouTube videos that are 30 minutes each in length. Please watch them then do the corresponding lesson. Great skills to you in your path to Japanese Literacy.

 - [Hiragana Lesson for Deck 01](https://www.youtube.com/watch?v=EKh9MQOaZ7I) - ん い く へ の け あ こ に
 - [Hiragana Lesson for Deck 02](https://www.youtube.com/watch?v=zdN5-vAb4yY) - り つ う ち ら た さ き
 - [Hiragana Lesson for Deck 03](https://www.youtube.com/watch?v=5zn3_fwShR0) - は ほ ま よ な お
 - [Hiragana Lesson for Deck 04](https://www.youtube.com/watch?v=3eITAScDoCY) - め ぬ ろ る わ れ ね す む
 - [Hiragana Lesson for Deck 05](https://www.youtube.com/watch?v=vGnKR3eX9m0) - し も て そ ゆ と え
 - [Hiragana Lesson for Deck 06](https://www.youtube.com/watch?v=Adp5SF451_s) - ひ や せ か み ふ を

Here's some more resources you might find useful:

 - [Hiragana pronunciation from TextFugu](http://www.textfugu.com/season-1/japanese-pronunciation/3-8/)
 - [Hiragana (with dakuten) pronunciation from TextFugu](http://www.textfugu.com/season-1/japanese-pronunciation/3-9/)
 - [Examples of handwritten hiragana](http://nihongo.as.ua.edu/hiragana.htm)
 - [Hiragana wiki page on Wikipedia](https://en.wikipedia.org/wiki/Hiragana)

### Using this course in Anki

Maybe I'll upload a complete `.apkg` file of these decks eventually, but for now here's what you need to do:

 - Import the audio files from `audio/` into your Anki media folder (see [this](https://apps.ankiweb.net/docs/manual.html#media18) and [this](https://apps.ankiweb.net/docs/manual.html#files) for help).
 - Create a new note type with fields: "Sort Order", "Romaji", "Kana", and "Audio".
 - Create three different cards for this note type (see "cards" below).
 - Make a new deck for this course.
 - In the options for the deck, I suggest selecting "Show cards in order added" so that you get cards in Memrise order. You can opt to show in random order, but you might get words before the hiragana characters themselves.
 - For each deck:
    - Become familiar with the hiragana characters you are about to learn. Watching the videos from above would be a good way to do this, or study them somehow on your own. Make sure you know how to pronounce them and write them with the correct stroke order *(along with the ["dakuten" and "handakuten" variants](https://en.wikipedia.org/wiki/Dakuten)!)*.
	- Optionally, make a sub-deck to import your cards into. You could also just import them all straight into a single deck when you're ready to study each level.
	- Import via `File --> Import` - Use the type and deck you just created, fields separated by comma. Fields 1, 2, 3, and 4 should be mapped to Sort Order, Romaji, Kana, and Audio (respectively).

### Cards

Obviously you can make your own if you want, but here's a good baseline template.

**Styling (shared between cards)**

```
.card {
 font-family: arial;
 font-size: 14px;
 text-align: center;
 color: black;
 background-color: white;
}
```

**Card 1 - Front Template**

```
Write<br><br>
<div style='font-family: Arial; font-size: 28px;'>{{Romaji}}</div>
<br>
in Hiragana.
```

**Card 1 - Back Template**

```
{{FrontSide}}

<hr id=answer>

<div style='font-family: Arial; font-size: 28px;'>{{Kana}}</div>
<br>
{{Audio}}
```

**Card 2 - Front Template**

```
Pronounce<br><br>
<div style='font-family: Arial; font-size: 28px;'>{{Kana}}</div>
<br>
```

**Card 2 - Back Template**

```
{{FrontSide}}

<hr id=answer>

<div style='font-family: Arial; font-size: 28px;'>{{Romaji}}</div>
<br>
{{Audio}}
```

**Card 3 - Front Template**

```
<div style='font-family: Arial; font-size: 28px;'>Write this audio using hiragana.</div>
<br>
{{Audio}}
<br>
(press 'r' to replay audio)
```

**Card 3 - Back Template**

```
{{FrontSide}}

<hr id=answer>

<div style='font-family: Arial; font-size: 28px;'>{{Kana}}</div>
<br>
{{Audio}}
```
