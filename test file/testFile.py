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


        print("\n\n =========================== NOT INDENTIFIED PROBLEM ============================= \n\n")

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