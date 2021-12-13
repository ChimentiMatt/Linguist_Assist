# Lingist Assist

#### https://spelling-assist.herokuapp.com/

##### A tool to help children, adults, native English speakers, and English as a second language learners improve their spelling and vocabulary.

## Hear words and thier definitions to see if you can get the word correctly

###### Select from pre-built lists, perfect for young learners, those trying to study for the SATs, or Adults. 

###### Select your missed words and see if you can get your words right this time around

###### Define how many rounds you want to play. The game's progress is dynamic, and the progress bar will match accordingly. 

## How it works

###### Lingust Assist is built with Django, Vue.js, and Sass.

###### It uses two apis. One to get the definitions of the words, and one to get the voice you hear in the game.

###### During the game, the app handles its post and fetches requests with Axios to not fresh the page. This process also allows the data to instantly be stored, and for further front-end manipulation.

###### In order to handle the thousands of words, another program was written to format words into accessible lists.  See the small python program here. https://github.com/ChimentiMatt/Python_Spelling_List_Converter It is tiny but powerful.

###### The 1st-grade through 9th-grade spelling lists were grabbed from educational resources. I then wrote a simple python program to parse the data (the words) I got online, putting each word into lists of strings. 

#### Have fun and let me know if you find any bugs, like my work, or have feed back http://www.matthewchim.com/, chimcode@gmail.com

