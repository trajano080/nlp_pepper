from os import abort
from GPSRparser import Parser


def tests():
    nlp = Parser.Parser()

    try:
        # simple actions
        action = nlp.classifier("follow skyler")
        assert action == "{'intent': 'follow', 'person': 'skyler'}\n"

        action = nlp.classifier("bring me the backpack")
        assert action == "{'intent': 'take', 'object': 'backpack', 'destination': 'me'}\n"

        action = nlp.classifier(
            "Navigate to the end table, meet alex, and follow her")
        assert action == "{'intent': 'go', 'destination': 'end table'}\n{'intent': 'to find someone', 'person': 'alex'}\n{'intent': 'follow', 'person': 'alex'}\n"

        action = nlp.classifier("move to the table")
        assert action == "{'intent': 'go', 'destination': 'table'}\n"

        action = nlp.classifier("take the cup to Valentin")
        assert action == "{'intent': 'take', 'object': 'cup', 'destination': 'valentin'}\n"

        action = nlp.classifier(
            "tell me the gender of the person in the corridor")
        assert action == "{'intent': 'say', 'who': 'me', 'what': 'the gender of the person in the corridor'}\n"

        action = nlp.classifier("meet william at the couch and follow him")
        assert action == "{'intent': 'go', 'destination': 'couch'}\n{'intent': 'to find someone', 'person': 'william'}\n{'intent': 'follow', 'person': 'william'}\n"

        action = nlp.classifier("find the cloth in the living room")
        assert action == "{'intent': 'go', 'destination': 'living room'}\n{'intent': 'to find something', 'object': 'cloth'}\n"

        action = nlp.classifier(
            "could you please bring me the orange from the end table")
        assert action == "{'intent': 'go', 'destination': 'end table'}\n{'intent': 'take', 'object': 'orange', 'destination': 'me'}\n"

        action = nlp.classifier(
            "tell me what's the smallest object on the bookcase")
        assert action == "{'intent': 'say', 'who': 'me', 'what': 'the smallest object on the bookcase'}\n"

        action = nlp.classifier(
            "Please tell me how many people in the kitchen are male")
        assert action == "{'intent': 'say', 'who': 'me', 'what': 'how many people in the kitchen are male'}\n"

        action = nlp.classifier(
            "Meet Francis at the entrance, follow her, and go to the bedroom")
        assert action == "{'intent': 'go', 'destination': 'entrance'}\n{'intent': 'to find someone', 'person': 'francis'}\n{'intent': 'follow', 'person': 'francis'}\n{'intent': 'go', 'destination': 'bedroom'}\n"

        action = nlp.classifier(
            "Robot please find the bowl in the living room")
        assert action == "{'intent': 'go', 'destination': 'living room'}\n{'intent': 'to find something', 'object': 'bowl'}\n"

        action = nlp.classifier("Could you follow Robin")
        assert action == "{'intent': 'follow', 'person': 'robin'}\n"

        action = nlp.classifier(
            "Could you please lead Jennifer from the couch to the bed")
        assert action == "{'intent': 'go', 'destination': 'couch'}\n{'intent': 'take', 'person': 'jennifer', 'destination': 'bed'}\n"

        action = nlp.classifier(
            "Escort Alex from the end table to the entrance")
        assert action == "{'intent': 'go', 'destination': 'end table'}\n{'intent': 'take', 'person': 'alex', 'destination': 'entrance'}\n"

        action = nlp.classifier(
            "Robot please follow Jennifer from the dining table to the bedroom")
        assert action == "{'intent': 'follow', 'person': 'jennifer'}\n"

        action = nlp.classifier(
            "Tell something about yourself to the person pointing to the right in the corridor")
        assert action == "{'intent': 'say', 'who': 'the person pointing to the right in the corridor', 'what': 'something about yourself'}\n"

        action = nlp.classifier("Please bring me the fruits")
        assert action == "{'intent': 'take', 'object': 'fruits', 'destination': 'me'}\n"

        action = nlp.classifier(
            "Navigate to the sink, meet Francis, and follow him")
        assert action == "{'intent': 'go', 'destination': 'sink'}\n{'intent': 'to find someone', 'person': 'francis'}\n{'intent': 'follow', 'person': 'francis'}\n"

        action = nlp.classifier(
            "Meet Alex at the dining table, follow him, and go to the dining room")
        assert action == "{'intent': 'go', 'destination': 'dining table'}\n{'intent': 'to find someone', 'person': 'alex'}\n{'intent': 'follow', 'person': 'alex'}\n{'intent': 'go', 'destination': 'dining room'}\n"

        action = nlp.classifier(
            "Could you follow Alex from the end table to the living room")
        assert action == "{'intent': 'follow', 'person': 'alex'}\n"

        action = nlp.classifier(
            "Could you please follow Jennifer from the sink to the dining room")
        assert action == "{'intent': 'follow', 'person': 'jennifer'}\n"

        action = nlp.classifier(
            "Go to the dishwasher, meet Robert, and follow him")
        assert action == "{'intent': 'go', 'destination': 'dishwasher'}\n{'intent': 'to find someone', 'person': 'robert'}\n{'intent': 'follow', 'person': 'robert'}\n"

        action = nlp.classifier(
            "Could you please meet William at the couch, follow him, and navigate to the dining room")
        assert action == "{'intent': 'go', 'destination': 'couch'}\n{'intent': 'to find someone', 'person': 'william'}\n{'intent': 'follow', 'person': 'william'}\n{'intent': 'go', 'destination': 'dining room'}\n"

        action = nlp.classifier("Follow Michael from the bed to the bedroom")
        assert action == "{'intent': 'follow', 'person': 'michael'}\n"

        action = nlp.classifier("Bring the cloth to the cupboard")
        assert action == "{'intent': 'take', 'object': 'cloth', 'destination': 'cupboard'}\n"

        action = nlp.classifier("Locate the tray in the living room")
        assert action == "{'intent': 'go', 'destination': 'living room'}\n{'intent': 'to find something', 'object': 'tray'}\n"

        action = nlp.classifier(
            "Tell me what's the biggest object on the end table")
        assert action == "{'intent': 'say', 'who': 'me', 'what': 'the biggest object on the end table'}\n"

        action = nlp.classifier("Tell me the gender of the person at the bed")
        assert action == "{'intent': 'say', 'who': 'me', 'what': 'the gender of the person at the bed'}\n"

        action = nlp.classifier(
            "Meet Mary at the dishwasher and escort her to the end table")
        assert action == "{'intent': 'go', 'destination': 'dishwasher'}\n{'intent': 'to find someone', 'person': 'mary'}\n{'intent': 'take', 'person': 'mary', 'destination': 'end table'}\n"

        action = nlp.classifier("Robot please find the drinks in the bedroom")
        assert action == "{'intent': 'go', 'destination': 'bedroom'}\n{'intent': 'to find something', 'object': 'drinks'}\n"

        action = nlp.classifier(
            "Tell me how many tray there are on the end table")
        assert action == "{'intent': 'say', 'who': 'me', 'what': 'how many tray there are on the end table'}\n"

        action = nlp.classifier(
            "Meet Patricia at the bed, follow her, and guide her back")
        assert action == "{'intent': 'go', 'destination': 'bed'}\n{'intent': 'to find someone', 'person': 'patricia'}\n{'intent': 'follow', 'person': 'patricia'}\n{'intent': 'take', 'person': 'patricia', 'destination': 'bed'}\n"

        action = nlp.classifier(
            "Could you please meet Jennifer at the sink, follow her, and guide her back")
        assert action == "{'intent': 'go', 'destination': 'sink'}\n{'intent': 'to find someone', 'person': 'jennifer'}\n{'intent': 'follow', 'person': 'jennifer'}\n{'intent': 'take', 'person': 'jennifer', 'destination': 'sink'}\n"

        action = nlp.classifier(
            "Grasp the cloth and place it on the storage table")
        assert action == "{'intent': 'take', 'object': 'cloth'}\n{'intent': 'place', 'object': 'cloth', 'destination': 'storage table'}\n"

        action = nlp.classifier(
            "Could you please meet Skyler at the exit, follow her, and take her back")
        assert action == "{'intent': 'go', 'destination': 'exit'}\n{'intent': 'to find someone', 'person': 'skyler'}\n{'intent': 'follow', 'person': 'skyler'}\n{'intent': 'take', 'person': 'skyler', 'destination': 'exit'}\n"

        action = nlp.classifier(
            "Could you please meet Linda at the end table, follow her, and take her back")
        assert action == "{'intent': 'go', 'destination': 'end table'}\n{'intent': 'to find someone', 'person': 'linda'}\n{'intent': 'follow', 'person': 'linda'}\n{'intent': 'take', 'person': 'linda', 'destination': 'end table'}\n"

        action = nlp.classifier(
            "Could you meet Linda at the bookcase, follow her, and take her back")
        assert action == "{'intent': 'go', 'destination': 'bookcase'}\n{'intent': 'to find someone', 'person': 'linda'}\n{'intent': 'follow', 'person': 'linda'}\n{'intent': 'take', 'person': 'linda', 'destination': 'bookcase'}\n"

        action = nlp.classifier(
            "Could you meet Michael at the sink, follow him, and lead him back")
        assert action == "{'intent': 'go', 'destination': 'sink'}\n{'intent': 'to find someone', 'person': 'michael'}\n{'intent': 'follow', 'person': 'michael'}\n{'intent': 'take', 'person': 'michael', 'destination': 'sink'}\n"

        action = nlp.classifier(
            "Could you meet Jennifer at the sink, follow her, and navigate to the dining room")
        assert action == "{'intent': 'go', 'destination': 'sink'}\n{'intent': 'to find someone', 'person': 'jennifer'}\n{'intent': 'follow', 'person': 'jennifer'}\n{'intent': 'go', 'destination': 'dining room'}\n"

        action = nlp.classifier(
            "Robot please give me the heaviest food from the bookcase")
        assert action == "{'intent': 'go', 'destination': 'bookcase'}\n{'intent': 'take', 'object': 'heaviest food', 'destination': 'me'}\n"

        action = nlp.classifier("Bring me the right most object from the sink")
        assert action == "{'intent': 'go', 'destination': 'sink'}\n{'intent': 'take', 'object': 'right most object', 'destination': 'me'}\n"

        action = nlp.classifier("Please locate three cutlery in the bedroom")
        assert action == "{'intent': 'go', 'destination': 'bedroom'}\n{'intent': 'to find something', 'object': 'three cutlery'}\n"

        action = nlp.classifier(
            "Give me the right most object from the end table")
        assert action == "{'intent': 'go', 'destination': 'end table'}\n{'intent': 'take', 'object': 'right most object', 'destination': 'me'}\n"

        action = nlp.classifier(
            "Bring me the right most object from the cupboard")
        assert action == "{'intent': 'go', 'destination': 'cupboard'}\n{'intent': 'take', 'object': 'right most object', 'destination': 'me'}\n"

        action = nlp.classifier(
            "Please give me the object above the sprite from the side table")
        assert action == "{'intent': 'go', 'destination': 'side table'}\n{'intent': 'take', 'object': 'object above the sprite', 'destination': 'me'}\n"

        action = nlp.classifier("Could you bring me the cleaning stuff")
        assert action == "{'intent': 'take', 'object': 'cleaning stuff', 'destination': 'me'}\n"

        action = nlp.classifier("Find William at the bed and ask him to leave")
        assert action == "{'intent': 'go', 'destination': 'bed'}\n{'intent': 'to find someone', 'person': 'william'}\n{'intent': 'say', 'who': 'william', 'what': 'leave'}\n"

        action = nlp.classifier(
            "Contact Mary at the dishwasher and ask her to leave")
        assert action == "{'intent': 'go', 'destination': 'dishwasher'}\n{'intent': 'to find someone', 'person': 'mary'}\n{'intent': 'say', 'who': 'mary', 'what': 'leave'}\n"

        action = nlp.classifier(
            "Meet Charlie at the bed, follow him, and navigate to the bedroom")
        assert action == "{'intent': 'go', 'destination': 'bed'}\n{'intent': 'to find someone', 'person': 'charlie'}\n{'intent': 'follow', 'person': 'charlie'}\n{'intent': 'go', 'destination': 'bedroom'}\n"

        action = nlp.classifier("Give me the orange from the cupboard")
        assert action == "{'intent': 'go', 'destination': 'cupboard'}\n{'intent': 'take', 'object': 'orange', 'destination': 'me'}\n"

        action = nlp.classifier("Take the coke to the sink")
        assert action == "{'intent': 'take', 'object': 'coke', 'destination': 'sink'}\n"

        action = nlp.classifier(
            "Could you please follow Alex from the dishwasher to the dining room")
        assert action == "{'intent': 'follow', 'person': 'alex'}\n"

        action = nlp.classifier("Could you give cleaning stuff to me")
        assert action == "{'intent': 'take', 'object': 'cleaning stuff', 'destination': 'me'}\n"

        action = nlp.classifier(
            "Meet Charlie at the sink and lead him to the bed")
        assert action == "{'intent': 'go', 'destination': 'sink'}\n{'intent': 'to find someone', 'person': 'charlie'}\n{'intent': 'take', 'person': 'charlie', 'destination': 'bed'}\n"

        action = nlp.classifier("Give cleaning stuff to me")
        assert action == "{'intent': 'take', 'object': 'cleaning stuff', 'destination': 'me'}\n"

        action = nlp.classifier(
            "Could you go to the bed, meet James, and escort him to the end table")
        assert action == "{'intent': 'go', 'destination': 'bed'}\n{'intent': 'to find someone', 'person': 'james'}\n{'intent': 'take', 'person': 'james', 'destination': 'end table'}\n"

        action = nlp.classifier(
            "Please navigate to the exit, meet Alex, and escort him to the dishwasher")
        assert action == "{'intent': 'go', 'destination': 'exit'}\n{'intent': 'to find someone', 'person': 'alex'}\n{'intent': 'take', 'person': 'alex', 'destination': 'dishwasher'}\n"

        action = nlp.classifier(
            "Accompany Charlie from the entrance to the end table")
        assert action == "{'intent': 'go', 'destination': 'entrance'}\n{'intent': 'take', 'person': 'charlie', 'destination': 'end table'}\n"

        action = nlp.classifier(
            "Robot please meet Skyler at the couch, follow her, and take her back")
        assert action == "{'intent': 'go', 'destination': 'couch'}\n{'intent': 'to find someone', 'person': 'skyler'}\n{'intent': 'follow', 'person': 'skyler'}\n{'intent': 'take', 'person': 'skyler', 'destination': 'couch'}\n"

        action = nlp.classifier(
            "Answer a question to the person raising their left arm in the living room")
        assert action == "{'intent': 'say', 'who': 'the person raising their left arm in the living room', 'what': 'a question'}\n"

        action = nlp.classifier(
            "Meet Francis at the bookcase, follow him, and go to the kitchen")
        assert action == "{'intent': 'go', 'destination': 'bookcase'}\n{'intent': 'to find someone', 'person': 'francis'}\n{'intent': 'follow', 'person': 'francis'}\n{'intent': 'go', 'destination': 'kitchen'}\n"

        action = nlp.classifier(
            "Tell me how many people in the dining room are standing")
        assert action == "{'intent': 'say', 'who': 'me', 'what': 'how many people in the dining room are standing'}\n"

        action = nlp.classifier(
            "Could you please bring me the thinnest food from the side table")
        assert action == "{'intent': 'go', 'destination': 'side table'}\n{'intent': 'take', 'object': 'thinnest food', 'destination': 'me'}\n"

        action = nlp.classifier(
            "Robot please meet William at the sink, follow him, and escort him back")
        assert action == "{'intent': 'go', 'destination': 'sink'}\n{'intent': 'to find someone', 'person': 'william'}\n{'intent': 'follow', 'person': 'william'}\n{'intent': 'take', 'person': 'william', 'destination': 'sink'}\n"

        action = nlp.classifier(
            "Could you please escort William from the exit to the bed")
        assert action == "{'intent': 'go', 'destination': 'exit'}\n{'intent': 'take', 'person': 'william', 'destination': 'bed'}\n"

        action = nlp.classifier("Please follow Charlie")
        assert action == "{'intent': 'follow', 'person': 'charlie'}\n"

        action = nlp.classifier(
            "Take the tray from the dining table and place it on the sink")
        assert action == "{'intent': 'go', 'destination': 'dining table'}\n{'intent': 'take', 'object': 'tray'}\n{'intent': 'place', 'object': 'tray', 'destination': 'sink'}\n"

        action = nlp.classifier("Find the fruits in the living room")
        assert action == "{'intent': 'go', 'destination': 'living room'}\n{'intent': 'to find something', 'object': 'fruits'}\n"

        action = nlp.classifier(
            "Go to the sink, meet William, and follow him")
        assert action == "{'intent': 'go', 'destination': 'sink'}\n{'intent': 'to find someone', 'person': 'william'}\n{'intent': 'follow', 'person': 'william'}\n"

        action = nlp.classifier("Find the fruits in the kitchen")
        assert action == "{'intent': 'go', 'destination': 'kitchen'}\n{'intent': 'to find something', 'object': 'fruits'}\n"

        action = nlp.classifier(
            "Robot please bring the dish to the dining table")
        assert action == "{'intent': 'take', 'object': 'dish', 'destination': 'dining table'}\n"

        action = nlp.classifier(
            "Accompany Mary from the dishwasher to the exit")
        assert action == "{'intent': 'go', 'destination': 'dishwasher'}\n{'intent': 'take', 'person': 'mary', 'destination': 'exit'}\n"

        action = nlp.classifier(
            "Could you please meet Michael at the dining table, follow him, and go to the corridor")
        assert action == "{'intent': 'go', 'destination': 'dining table'}\n{'intent': 'to find someone', 'person': 'michael'}\n{'intent': 'follow', 'person': 'michael'}\n{'intent': 'go', 'destination': 'corridor'}\n"

        action = nlp.classifier(
            "Tell me which are the three thinnest cutlery on the storage table")
        assert action == "{'intent': 'say', 'who': 'me', 'what': 'which are the three thinnest cutlery on the storage table'}\n"

        action = nlp.classifier(
            "Go to the bed, meet Robin, and take her to the exit")
        assert action == "{'intent': 'go', 'destination': 'bed'}\n{'intent': 'to find someone', 'person': 'robin'}\n{'intent': 'take', 'person': 'robin', 'destination': 'exit'}\n"

        action = nlp.classifier(
            "Tell me how many people in the dining room are sitting")
        assert action == "{'intent': 'say', 'who': 'me', 'what': 'how many people in the dining room are sitting'}\n"

        action = nlp.classifier(
            "Could you please grasp the tray and place it on the end table")
        assert action == "{'intent': 'take', 'object': 'tray'}\n{'intent': 'place', 'object': 'tray', 'destination': 'end table'}\n"

        action = nlp.classifier(
            "Meet John at the exit and escort him to the end table")
        assert action == "{'intent': 'go', 'destination': 'exit'}\n{'intent': 'to find someone', 'person': 'john'}\n{'intent': 'take', 'person': 'john', 'destination': 'end table'}\n"

        action = nlp.classifier(
            "Robot please accompany Francis from the dishwasher to the sink")
        assert action == "{'intent': 'go', 'destination': 'dishwasher'}\n{'intent': 'take', 'person': 'francis', 'destination': 'sink'}\n"

        action = nlp.classifier(
            "Could you please meet John at the dishwasher and follow him")
        assert action == "{'intent': 'go', 'destination': 'dishwasher'}\n{'intent': 'to find someone', 'person': 'john'}\n{'intent': 'follow', 'person': 'john'}\n"

        print("\n\n ===================================== DEBATABLE ======================================== \n\n")

        action = nlp.classifier(
            "Face William at the couch and accompany him to his taxi")
        print(action)
        #assert action == "{}\n"

        print("\n\n =========================== OBJECTS DESCRIPTIONS'S PROBLEM ============================= \n\n")

        action = nlp.classifier(
            "Navigate to the dining room, find a person pointing to the left, and say the day of the month")
        print(action)
        #assert action == "{}\n"
        action = nlp.classifier(
            "Could you go to the bedroom, locate a person pointing to the left, and answer a question")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Could you find a person pointing to the right in the living room and tell the time")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Robot please deliver cutlery to the person raising their left arm in the dining room")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Navigate to the dining room, look for a person pointing to the left, and say your team's name")
        print(action)
        #assert action == "{}\n"

        print("\n\n =============================== ORDEN INVERTIDO ================================= \n\n")

        action = nlp.classifier(
            "Lead John to the couch, you can find him at the bed")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Take John to the bed, you will find him at the bed")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Escort Alex to the entrance, you may find her at the end table")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Escort Charlie to the end table, you will find him at the sink")
        print(action)
        #assert action == "{}\n"

        print("\n\n =========================== NOT INDENTIFIED PROBLEM ============================= \n\n")

        action = nlp.classifier(
            "Provide drinks to everyone in the kitchen.")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Go to the exit, meet Charlie, and escort him")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Go to the sink, locate the tray, and give it to Francis at the end table")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Grasp the paprika and put it on the cupboard")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Go to the sink, look for the paprika, and deliver it to Francis at the bed")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Robot please get the cloth and put it on the side table")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Go to the dishwasher, meet Jennifer, and escort her")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier("Dump the litter")
        print(action)
        #assert action == "{}\n"


        action = nlp.classifier(
            "Face Robert at the dining table and introduce it to Linda at the desk")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier("Take out the trash")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Greet James at the rear door and introduce him to everyone in the living room.")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Could you please face William at the end table and introduce it to Skyler at the bed")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Contact Elizabeth at the dining table and introduce it to Patricia at the couch")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier(
            "Greet Robin at the front door and introduce him to all the children in the corridor.")
        print(action)
        #assert action == "{}\n"

        action = nlp.classifier("Take out the debris")
        print(action)
        #assert action == "{}\n"

    except AssertionError as e:
        print(action)
        raise e


if __name__ == "__main__":
    try:
        tests()
    except Exception as e:
        raise e
