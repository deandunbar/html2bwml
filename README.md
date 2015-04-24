# html2bwml


POC application that automatically converts bootstrap based webpages into Bitwave Markup Language (BWML). Images are compressed and base 64 encoded into in-line source. External links are uploaded to the storj.io netowrk. The link is replaced by a file hash that is stored in the florincoin blockchain. The link changes from an anchor to a wave link tag. The wave link tag follows links with the local Bitwave proxy


Python application that parses an html document and is able to convert said document to bwml (bitwave markup language) for use with bitwave application. 

The bwml is a custom html document that replaces all links with the strj file hash equivalent. Custom data information is added inside the document. 
