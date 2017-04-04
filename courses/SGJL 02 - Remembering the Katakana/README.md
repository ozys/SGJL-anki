# SGJL 02 - Remembering the Katakana

### Course notes:

Part 2 of the Remembering the Kana series. After this course, the evil that is romaji will no longer be needed.

This course assumes that you've completed SGJL01 and are familiar with Hiragana. If you aren't yet familiar with Hiragana, I suggest waiting until you are to start this course.

This course is **NOT** about learning new words. Don't worry about learning what the words mean; instead, the course uses authentic Japanese words as example pronunciations to reinforce understanding both spoken and written kana. The test lessons should therefore go much, much quicker as each example word will **ONLY** use kana that was previously learned in the lessons.

Each kana course will have six YouTube videos that are 30 minutes each in length. Please watch them then do the following lesson. Great skills to you in your path to Japanese Literacy.

 - [Katakana Lesson for Deck 01](https://www.youtube.com/watch?v=QG8vyoTWmwg) - リ ー ヘ カ キ ソ セ ヤ ャ ナ
 - [Katakana Lesson for Deck 02](https://www.youtube.com/watch?v=rkdeo-YzYfw) - ニ チ ベ ハ パ ミ
 - [Katakana Lesson for Deck 03](https://www.youtube.com/watch?v=jTxFa3k7R_k) - コ ツ シ ン モ ノ メ
 - [Katakana Lesson for Deck 04](https://www.youtube.com/watch?v=bJk4unKv0Pw) - フ ス ヌ ラ ヲ 久 タ ワ ウ
 - [Katakana Lesson for Deck 05](https://www.youtube.com/watch?v=kxAmzq_wnZM) - ホ オ ル レ テ ケ マ ム ア
 - [Katakana Lesson for Deck 06](https://www.youtube.com/watch?v=uhA6Lf8dHXo) - ユ イ ロ ヨ ト ヒ サ エ ネ

Here's some more resources you might find useful:

 - [Hiragana pronunciation from TextFugu](http://www.textfugu.com/season-1/japanese-pronunciation/3-8/) - Katakana use the same pronunciation
 - [Hiragana (with dakuten) pronunciation from TextFugu](http://www.textfugu.com/season-1/japanese-pronunciation/3-9/) - Katakana use the same pronunciation
 - [Examples of handwritten katakana](http://nihongo.as.ua.edu/katakana.htm)
 - [Katakana wiki page on Wikipedia](https://en.wikipedia.org/wiki/Katakana) - You can click on each kana to see a stroke order

### Using this course in Anki

I'll upload a complete `.apkg` file of these decks eventually, but for now here's what you need to do:

 - Import the audio files from `audio/` into your Anki media folder (see [this](https://apps.ankiweb.net/docs/manual.html#media18) and [this](https://apps.ankiweb.net/docs/manual.html#files) for help).
 - Create a new note type with fields: "Sort Order", "Hiragana", "Katakana", and "Audio".
 - Create three different cards for this note type (see "cards" below).
 - Make a new deck for this course.
 - For each `.txt` file in this folder:
    - Become familiar with the katakana characters you are about to learn. Watching the videos from above would be a good way to do this, or study them somehow on your own. Make sure you know how to pronounce them and write them with the correct stroke order *(along with the ["dakuten" and "handakuten" variants](https://en.wikipedia.org/wiki/Dakuten)!)*.
	- Optionally, make a sub-deck to import your cards into. You could alternatively just import each one straight into a single deck when you're ready to study each level.
	- Import via `File --> Import` - Use the type and deck you just created, fields separated by comma. Fields 1, 2, 3, and 4 should be mapped to Sort Order, Hiragana, Katakana, and Audio (respectively).

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
<div style='font-family: Arial; font-size: 28px;'>{{Hiragana}}</div>
<br>
using katakana.
```

**Card 1 - Back Template**

```
{{FrontSide}}

<hr id=answer>

<div style='font-family: Arial; font-size: 28px;'>{{Katakana}}</div>
<br>
{{Audio}}
```

**Card 2 - Front Template**

```
Pronounce<br><br>
<div style='font-family: Arial; font-size: 28px;'>{{Katakana}}</div>
<br>
```

**Card 2 - Back Template**

```
{{FrontSide}}

<hr id=answer>

<div style='font-family: Arial; font-size: 28px;'>{{Hiragana}}</div>
<br>
{{Audio}}
```

**Card 3 - Front Template**

```
<div style='font-family: Arial; font-size: 28px;'>Write this audio using katakana.</div>
<br>
{{Audio}}
<br>
(press 'r' to replay audio)
```

**Card 3 - Back Template**

```
{{FrontSide}}

<hr id=answer>

<div style='font-family: Arial; font-size: 28px;'>{{Katakana}}</div>
<br>
{{Audio}}
```
