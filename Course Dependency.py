from collections import defaultdict, deque

class VideoCoursePlatform:
    def __init__(self):
        self.graph = defaultdict(list)
        self.completed_courses = set()

    def add_course(self, course, prerequisites=None):
        if prerequisites is None:
            prerequisites = []
        self.graph[course] = prerequisites

    def enroll(self, course):
        if course not in self.graph:
            return "Course not found."
        if course in self.completed_courses:
            return "Course already completed."
        if not self.has_uncompleted_prerequisites(course):
            self.completed_courses.add(course)
            return f"Successfully enrolled in {course}."
        return "Prerequisites not completed."

    def resolve_prerequisites(self):
        graph_copy = self.graph.copy()

        queue = deque(course for course, prereqs in graph_copy.items() if not prereqs)

        completion_order = []

        while queue:
            course = queue.popleft()
            completion_order.append(course) 

            for dependent_course, prerequisites in graph_copy.items():
                if course in prerequisites:
                    prerequisites.remove(course)
                    if not prerequisites:
                        queue.append(dependent_course)

        if len(completion_order) != len(self.graph):
            return "Circular dependencies exist, cannot resolve prerequisites."

        return completion_order

    def has_uncompleted_prerequisites(self, course):
        for prereq in self.graph[course]:
            if prereq not in self.completed_courses:
                return True
        return False

x = VideoCoursePlatform()
x.add_course('C')
x.add_course('C++', prerequisites=['C'])
x.add_course('Java', prerequisites=['C++'])
x.add_course('Java Script', prerequisites=['C', 'Java'])
x.add_course('React', prerequisites=['Java Script'])
x.add_course('Python', prerequisites=['Java'])

print(x.enroll('C'))  
print(x.enroll('C++'))  
print(x.enroll('Java')) 
print(x.enroll('Java Script'))
print(x.enroll('React'))  
print(x.enroll('Python'))  

print(x.resolve_prerequisites())