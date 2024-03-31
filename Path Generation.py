import random

class PathGenerator:
    def __init__(self, courses_data, user_data):
        self.courses_data = courses_data
        self.user_data = user_data

    def generate_learning_path(self, user_id, num_recommendations=5):
        past_engagements = self.user_data.get(user_id, [])
        
        user_interests = self.analyze_interests(past_engagements)
        
        recommendations = self.generate_recommendations(user_interests, num_recommendations)
        
        return recommendations

    def analyze_interests(self, past_engagements):
        interests = {}
        for engagement in past_engagements:
            course_id = engagement['course_id']
            course_topic = self.courses_data[course_id]['topic']
            interests[course_topic] = interests.get(course_topic, 0) + 1
        
        return interests

    def generate_recommendations(self, user_interests, num_recommendations):
        ranked_courses = list(user_interests.keys())
        random.shuffle(ranked_courses)

        recommendations = ranked_courses[:num_recommendations]
        
        return recommendations

#Test Case

courses_data = {
        'course1': {'topic': 'Python Programming'},
        'course2': {'topic': 'Data Science'},
        'course3': {'topic': 'Machine Learning'},
   }

user_data = {
    'user1': [{'course_id': 'course1', 'performance': 'good'}, {'course_id': 'course2', 'performance': 'excellent'}],
}

learning_path_generator = PathGenerator(courses_data, user_data)

user_id = 'user1'
learning_path = learning_path_generator.generate_learning_path(user_id)
print("Recommended Learning Path for User:", learning_path)