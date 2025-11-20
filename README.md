The dataset file consists of two colmuns the first one is the thesis title in English and the second colmuns is the thesis title in Arabic .\
The following preprocessing steps have been implemented for both English and Arabic texts:- \
English sentences:\
-Apply lowercase to all text: this increases model performance and consistency, decreases the amount of vocabulary, and improves tokenization matching.\
 -Replace special symbols and digits with equivalent words. This reduces noise and improves the sentence readability.
Arabic sentences:\
-Normalizing the letters to decrease the amount of vocabulary, because they have the same meaning in English as follows: \
    - The letter(ى) Alif Maqsura is normalized to  (ي) Yaa.\
    - The(ة)  ta marbouta  is normalized to Ha.\
    - The different forms of the letter (أ - اً - إ) alef is normalized to (ا).


The dataset can be used for:\
1-Machine Translation (MT).\
2-Summarization.\
3-Sentiment or Classification Tasks.\
4-Preserving academic research for a long time by turning theses into organized, machine-readable datasets.
