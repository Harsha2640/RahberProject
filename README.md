# Course Dependency Resolutiion(Task 1):

I have imported "defaultdict" to creates a dictionary-like object to automatically create that key and assign it a default value specified during its initialization. It will be None if no value is provided.
I have imported "deque" from 'collections' as it a best way to append and pop from both ends, offering advantages in terms of performance and memory efficiency.

1. I  used a combination of graph approach with topological sorting, and i also implemented a second approach to enroll the courses that have no prerequisites or prerequisites that have already been completed.

2. So, i defined a class "VideoCoursePlatform" that contains a graphical representation of courses and their prerequisites.

3. I defined the method "add_course" to add the courses with their prerequisites to the platform.

4. I defined the method "enroll" to allow the user to enroll in the course and to check if the prerequisites are completed before the enrollment.

5. I defined the method "resolve_prerequisites" to resolve the prerequisites using a topological sorting to determine the optimized learning path.

6. I defined "has_uncompleted_prerequisites" method to check wether the prerequisites been completed for the particular course or not.7

7. I have added a test case below the code to check if a particular course can be completed without the prerequisites been completed.



# Personalized Learning Path Generation(Task 3):

1. I have imported the built-in function "random" module to generate the random numbers which in used in the code for simulation purpose.

2. I created a class "Path Generator" in which it contains the details of the course and the user.

3. I defined a method to generate the learning path to retrieve user information based on recomendation's. Initially i have set the number of recomendation's to 5 to retrieve the user's past registration's and the performance records of the user's.

4. Then i have analyzed the user's interests based on their past engagements and generated the personalized recommendations based on the interests.

5. Then i have added a method "analyze_interests" to count and analyze the occurrences of the topics, in this method i have written the code assuming the word 'topic' in each course's data.

6. Then i have intialized a method "generate recommendations" to rank the courses based user's interests and for recommending the top courses.

7. I have also added the test case for the generating the output by adding the courses and the user data by this both the data present we can initialize the learning path generator for the user




# System Architechture for Scalable Video Streaming(Task 2):

To Implement a system architecture for streaming educational content with low latency, high availability, and adaptive streaming quality requires careful consideration of several components. Here's a brief  step by step architectural proposal:

•	Python libraries like Django or Flask can be used to build a content management system (CMS) for handling educational content. The CMS should allow uploading, processing, and organizing videos efficiently.

•	Using a content delivery network (CDN) like Amazon CloudFront or Cloudflare can help cache and deliver content to users around the world with low delay. CDNs distribute content closer to users, reducing the load on the main server and improving content availability.

•	Services like FFmpeg or AWS Elemental Media Convert can be used for transcoding videos into multiple bitrates and resolutions. Adaptive bitrate streaming allows users with varying internet speeds to watch content smoothly by adjusting the quality based on their connection.

•	Use tools like Nginx or HAProxy to spread incoming traffic across multiple servers. This ensures high availability and scalability during busy times.

•	Employ edge computing technologies like AWS Lambda@Edge or Cloudflare Workers to run code closer to users, reducing delay. Edge computing can be used for Realtime video processing, such as ad insertion or DRM encryption.

•	Implement secure user authentication and authorization using OAuth, JWT, or OpenID Connect. This ensures only authorized users can access premium content and helps track user activity.

•	Integrate monitoring tools like Promethe­us, Grafana, or AWS CloudWatch to get real-time data on system health, performance, and user engagement metrics. Analytics help understand user be­havior and identify performance issues.

•	Utilize different server locations with backup systems to ensure the content is always available and can withstand issues in any single region. Store content closer to users in various regions through geographical replication.

•	Use machine learning techniques to provide personalized content suggestions based on user preferences, viewing history, and engagement data. Tools like TensorFlow or PyTorch can help build these recommendation engines.

•	Set up automated testing, deployment, and scaling processes using CI/CD tools like Jenkins, GitLab CI, or AWS Code Pipeline. This allows for faster updates, quicker bug fixes, and seamless rollout of new features.

•	Implement Digital Rights Management (DRM) solutions such as Widevine, FairPlay, or PlayReady to protect copyrighted content from unauthorized access and piracy.
