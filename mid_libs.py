import streamlit as st

def generate_story(name, place, animal, food, emotion, activity):
    story = f"""
    One day, {name} went to {place} and saw a {animal}. 
    The {animal} was eating {food} and looked very {emotion}. 
    {name} decided to join the {animal} and they both enjoyed {activity} together. 
    It was the best day ever!
    """
    return story

def main():
    st.title("Mad Libs Story Generator")
    st.subheader("Fill in the blanks to create your own story!")
    
    name = st.text_input("Enter a name:")
    place = st.text_input("Enter a place:")
    animal = st.text_input("Enter an animal:")
    food = st.text_input("Enter a type of food:")
    emotion = st.text_input("Enter an emotion:")
    activity = st.text_input("Enter an activity:")
    
    if st.button("Generate Story"):
        if name and place and animal and food and emotion and activity:
            story = generate_story(name, place, animal, food, emotion, activity)
            st.subheader("Your Story:")
            st.write(story)
        else:
            st.warning("Please fill in all the fields before generating the story.")

if __name__ == "__main__":
    main()
