import string
import os
import socket

def main():
    with open("/home/output/result.txt", "w+") as result_file:
        path = "/home/data"
        dir_list = os.listdir(path)
        result_file.write("All the files in /home/data are as follows:- " + path)
        for file_name in dir_list:
            result_file.write("\n" + file_name)
        
        with open('/home/data/IF.txt','r') as if_file:
            if_data = if_file.read()
            if_words = if_data.split()
            if_words = [word.translate(str.maketrans('', '', string.punctuation)).capitalize() for word in if_words]
            result_file.write("\nIF.txt has a word count of:- " + str(len(if_words)))
        
        with open('/home/data/Limerick.txt','r') as lime_file:
            lime_data = lime_file.read()
            lime_words = lime_data.split()
            result_file.write("\nLimerick.txt has a word count of:- " + str(len(lime_words)))
        
        allwords = if_words + lime_words
        result_file.write("\nTotal number of words in IF.txt and Limerick.txt are:- " + str(len(allwords)))
        
        count_if_words = {}
        for word in if_words:
            count_if_words[word] = count_if_words.get(word, 0) + 1
        
        top_words = sorted(count_if_words.items(), key=lambda x: x[1], reverse=True)[:3]
        result_file.write("\nThe top 3 words with maximum number of counts in IF.txt are:- ")
        for word, count in top_words:
            result_file.write("\n" + word + " - " + str(count))
        
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        result_file.write("\nDocker machine IP Address is:" + ip_address)
    
    with open('/home/output/result.txt','r') as result_file:
        data_res = result_file.read()
        print(data_res)

if __name__ == "__main__":
    main()
