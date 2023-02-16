# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List


from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

shoppinglist=[]

class ActionCreateShoppingList(Action):

    shoppinglist = []

    
        

    def name(self) -> Text:
        return "action_create_shopping_list"
      
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        user_choice = next(tracker.get_latest_entity_values("shopping_items"), None)
        ActionCreateShoppingList.shoppinglist.append(user_choice)
        dispatcher.utter_message(text=f"{user_choice} added successfully")    
        return []


class ActionRemoveFromShoppingList(Action):

    obj1 = ActionCreateShoppingList()

    

    def name(self) -> Text:
        return "action_remove_from_shopping_list"
      
    def run(self, dispatcher: CollectingDispatcher,  tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        remove_user_choice = next(tracker.get_latest_entity_values("remove_shopping_items"), None)
        ActionRemoveFromShoppingList.obj1.shoppinglist.remove(remove_user_choice)
        dispatcher.utter_message(text=f"You removed {remove_user_choice}")
      
        return []


class ActionViewShoppingList(Action):

    obj2 = ActionCreateShoppingList()


    def name(self) -> Text:
        return "action_view_shopping_list"
      
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        


        finallist = list(zip(ActionViewShoppingList.obj2.shoppinglist))
        dispatcher.utter_message(text = f"{finallist}")

    
        return []
       



