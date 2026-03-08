import json
import os
import re

# Output directory
out_dir = r"C:\Users\hp\.gemini\antigravity\scratch\issb-prep\src\data"
os.makedirs(out_dir, exist_ok=True)

essays_text = """Kashmir Issue and Its Solution
Terrorism in Pakistan
Role of Army in National Development
Corruption in Pakistan
Energy Crisis in Pakistan
Load Shedding and Its Effects
Water Crisis in Pakistan
Poverty in Pakistan
Unemployment in Pakistan
Inflation and Its Effects on Common Man
Role of Youth in Nation Building
Importance of Education
Technical Education in Pakistan
Brain Drain Causes and Remedies
Student Politics Pros and Cons
Role of Media in Education
Pakistan Armed Forces Defenders of the Nation
Nuclear Pakistan Responsibilities
Importance of National Unity
Hybrid Warfare Threat to Pakistan
Fifth Generation Warfare
CPEC and Its Importance
Drug Addiction Among Youth
Child Labor in Pakistan
Women Empowerment in Pakistan
Role of Women in Society
Population Explosion in Pakistan
Sectarianism in Pakistan
Artificial Intelligence Boon or Bane
Social Media Advantages and Disadvantages
Climate Change and Pakistan
Deforestation and Its Effects
Importance of Sports in Life
Leadership Qualities of a Good Officer
Discipline the Key to Success
Importance of Time Management
Patriotism and Its Importance
Honesty the Best Policy
Character Building in Youth
Self Confidence and Personality Development
Globalization and Its Impact on Pakistan
Democracy in Pakistan
Role of NGOs in Pakistan
Media Fourth Pillar of State
Importance of Agriculture in Pakistan
Pakistan China Relations
Pakistan USA Relations
Pakistan India Relations
Pakistan Afghanistan Relations
Role of Pakistan in UN Peacekeeping Missions
OIC and Muslim Unity
SCO and Pakistan Role
Belt and Road Initiative
Importance of Diplomacy
Pakistan Foreign Policy Challenges
CPEC Gateway to Prosperity
IMF and Pakistan Economy
Privatization Pros and Cons
Foreign Direct Investment in Pakistan
Small and Medium Enterprises in Pakistan
Stock Exchange and Economy
Black Economy in Pakistan
Remittances and Pakistan Economy
Fiscal Deficit Causes and Solutions
Role of Banking Sector in Development
Good Governance in Pakistan
Accountability and Rule of Law
Electoral Reforms in Pakistan
Decentralization of Power
Role of Judiciary in Pakistan
Police Reforms in Pakistan
Local Government System
Constitution of Pakistan Importance
Political Instability in Pakistan
Health Crisis in Pakistan
Polio Eradication Challenges
COVID 19 Lessons
Mental Health Awareness
Malnutrition in Pakistan
Role of Doctors in Society
Public vs Private Healthcare
Clean Water and Sanitation
Maternal Mortality in Pakistan
Importance of Physical Fitness
Islam and Science
Role of Religion in Modern Life
Tolerance in Islam
Islamic Banking in Pakistan
Ethics in Public Life
Extremism vs Moderation
Quaid e Azam Vision for Pakistan
Allama Iqbal Message for Youth
Two Nation Theory Today
Space Technology and Pakistan
Biotechnology Future
Information Technology in Pakistan
Cyber Security Importance
Renewable Energy Future
Electric Vehicles Future
Robotics and Automation
E Commerce in Pakistan
Digital Pakistan Initiative
Research and Development Importance
Floods in Pakistan Causes and Management
Earthquake Preparedness
Glaciers of Pakistan
Billion Tree Project
Urbanization Problems
Blue Economy Importance
Indus Water Treaty
Smog Crisis in Punjab
Waste Management in Cities
Wetlands Importance
Inter Services Cooperation
Army Role in Disaster Management
Operation Zarb e Azb
Operation Radd ul Fasaad
Nuclear Deterrence
Intelligence Agencies Role
Psychological Warfare
Military Diplomacy
Gwadar Strategic Importance
Maritime Security
Great Leaders of Pakistan
Importance of Teamwork
Decision Making Under Pressure
Emotional Intelligence
Servant Leadership
Role of Soldier in Society
Sacrifice for Nation
Mentorship Importance
Self Discipline and Success
Motivation in Leadership
Fake News Threat
Freedom of Press
Social Media in Politics
Propaganda and Counter Narrative
Digital Journalism
Film and Drama Impact
Importance of Urdu Language
Books Role in Life
Public Speaking Importance
Communication Skills Importance
Pakistan Movement Lessons
Cultural Diversity of Pakistan
Sports Diplomacy
Cricket and National Identity
Museums and Heritage
Defence Day Importance
Pakistan Day Importance
Lessons from History
Golden Era of Islam
Overpopulation and Food Security
Importance of Volunteerism
NGOs and Civil Society
Saving Money Importance
Rural Development in Pakistan
Microfinance and Poverty Reduction
Importance of Census
Pakistan Vision 2050
My Ideal Pakistan
Geopolitical Importance of Pakistan
Afghanistan Crisis and Pakistan
Iran Pakistan Relations
Saudi Arabia Vision 2030 and Pakistan
Palestine Issue
Russia Ukraine War Impact
Rise of China
India Hegemony in South Asia
Global Warming Responsibility
United Nations Role Today
G20 and Developing Countries
Artificial Islands Strategic Importance
Maritime Silk Road
Arctic Future Conflicts
Space Race
Quantum Computing
Gene Editing Ethics
Metaverse Future
ChatGPT and Future Jobs
Pakistan Economic Future
Justice Delayed is Justice Denied
Importance of Trees
Traffic Problems in Cities
Child Rights in Pakistan
Old Age Homes Need or Shame
Importance of Punctuality
Hard Work vs Smart Work
Failure a Stepping Stone
Reading Habit in Youth
Importance of Mother Tongue
Role of Teachers in Society
Peer Pressure on Students
Importance of Family Values
Mobile Phone Addiction
Importance of Saving Money
Rural Development
Importance of Justice
Youth Problems in Pakistan
Pakistan Path to Prosperity"""

sct_eng_text = """  1.  I am happiest when ___________
  2.  My greatest strength is ___________
  3.  My biggest weakness is ___________
  4.  People who know me say I am ___________
  5.  I feel proud when ___________
  6.  I feel ashamed when ___________
  7.  My best quality is ___________
  8.  Others think of me as ___________
  9.  I consider myself to be ___________
 10.  I become nervous when ___________
 11.  I lose my temper when ___________
 12.  I am at my best when ___________
 13.  My most important characteristic is ___________
 14.  I feel most confident when ___________
 15.  I am not good at ___________
 16.  When I am alone, I ___________
 17.  I feel inferior when ___________
 18.  The thing I dislike most about myself is ___________
 19.  My personality can best be described as ___________
 20.  I usually react to criticism by ___________
FAMILY
 21.  My father is ___________
 22.  My mother is ___________
 23.  My family means ___________
 24.  At home, I usually ___________
 25.  My parents always ___________
 26.  I wish my father would ___________
 27.  I wish my mother would ___________
 28.  My relationship with my family is ___________
 29.  My parents have taught me ___________
 30.  My siblings and I ___________
 31.  My father taught me ___________
 32.  At home, the atmosphere is ___________
 33.  My parents always wanted me to ___________
 34.  I learned discipline from ___________
 35.  My family background has ___________
FRIENDS & SOCIAL LIFE
 36.  My best friend is ___________
 37.  I get along well with ___________
 38.  I find it difficult to mix with ___________
 39.  My friends think I am ___________
 40.  When in a group, I usually ___________
 41.  I make friends ___________
 42.  I prefer friends who are ___________
 43.  I enjoy social gatherings because ___________
 44.  I find it hard to talk to ___________
 45.  Most of my friends are ___________
 46.  I trust people who ___________
 47.  I feel uncomfortable when people ___________
 48.  To get along with others, I ___________
 49.  People avoid me when I ___________
 50.  I am liked by others because ___________
LEADERSHIP & AUTHORITY
 51.  A good leader should ___________
 52.  When given authority, I ___________
 53.  I follow orders when ___________
 54.  I would make a good officer because ___________
 55.  When I lead a group, I ___________
 56.  I respect authority because ___________
 57.  A commander should always ___________
 58.  I can motivate others by ___________
 59.  The best way to lead is ___________
 60.  Discipline means ___________
 61.  I would describe my leadership style as ___________
 62.  When my team fails, I ___________
 63.  A senior officer should ___________
 64.  I believe in taking initiative because ___________
 65.  When given responsibility, I feel ___________
MILITARY & NATIONAL SERVICE
 66.  I want to join the army because ___________
 67.  Military life ___________
 68.  My motivation to become an officer is ___________
 69.  Pakistan Army is ___________
 70.  Serving the nation means ___________
 71.  An army officer must ___________
 72.  The defense of Pakistan is ___________
 73.  I believe patriotism is ___________
 74.  A soldier must ___________
 75.  My aim in joining the armed forces is ___________
 76.  I chose the military profession because ___________
 77.  Uniform to me represents ___________
 78.  Pakistan's security depends on ___________
 79.  Life in uniform is ___________
 80.  I am prepared for military service because ___________
EDUCATION & STUDIES
 81.  My studies have been ___________
 82.  At school, I was ___________
 83.  My favorite subject is ___________
 84.  Education for me means ___________
 85.  I perform best academically when ___________
 86.  My teachers always said that I ___________
 87.  The subject I find most difficult is ___________
 88.  My academic performance has been ___________
 89.  I enjoy learning ___________
 90.  When studying, I ___________
EMOTIONS & STRESS MANAGEMENT
 91.  Under pressure, I ___________
 92.  When I fail, I ___________
 93.  I feel stressed when ___________
 94.  I deal with failure by ___________
 95.  When things go wrong, I ___________
 96.  I feel frustrated when ___________
 97.  I control my emotions by ___________
 98.  My biggest fear is ___________
 99.  I feel lonely when ___________
100.  When I am depressed, I ___________
101.  I feel anxiety when ___________
102.  I overcome fear by ___________
103.  When someone hurts me, I ___________
104.  I become upset when ___________
105.  I stay calm under pressure by ___________
AMBITIONS & GOALS
106.  My ambition in life is ___________
107.  In ten years, I want to be ___________
108.  My goal in life is ___________
109.  I am working towards ___________
110.  I want to achieve ___________
111.  My dream is ___________
112.  I want to be remembered as ___________
113.  Success for me means ___________
114.  My biggest aspiration is ___________
115.  To succeed in life, one must ___________
116.  I will achieve my goals by ___________
117.  The most important thing in life is ___________
118.  I measure success by ___________
119.  My future plans are ___________
120.  To be successful, I need to ___________
CHALLENGES & ADVERSITY
121.  Hardship makes me ___________
122.  The most difficult situation I faced was ___________
123.  I have overcome difficulties by ___________
124.  When faced with a challenge, I ___________
125.  Obstacles in life make me ___________
126.  I have learned from my failures that ___________
127.  When life gets tough, I ___________
128.  The biggest challenge I faced was ___________
129.  Adversity teaches me ___________
130.  I deal with problems by ___________
TEAMWORK & COOPERATION
131.  Working in a team ___________
132.  I cooperate with others by ___________
133.  A good team player should ___________
134.  When someone disagrees with me, I ___________
135.  Group tasks are ___________
136.  I contribute to a team by ___________
137.  Teamwork is important because ___________
138.  When my team succeeds, I ___________
139.  I prefer working ___________
140.  Conflicts in a team should be ___________
VALUES & ETHICS
141.  Honesty to me means ___________
142.  I believe in ___________
143.  Integrity is ___________
144.  My values in life are ___________
145.  I consider it wrong to ___________
146.  Loyalty means ___________
147.  Moral courage is ___________
148.  I believe in honesty because ___________
149.  Ethics in a profession means ___________
150.  Courage to me means ___________
PHYSICAL FITNESS & SPORTS
151.  Physical fitness is ___________
152.  My favorite sport is ___________
153.  I believe sports teach ___________
154.  Physical training for me is ___________
155.  I maintain my fitness by ___________
156.  Sports have taught me ___________
157.  Being physically fit helps me ___________
158.  I exercise because ___________
159.  My physical endurance is ___________
160.  Competitive sports make me ___________
DECISION MAKING
161.  When making a difficult decision, I ___________
162.  I take decisions by ___________
163.  Quick decisions are ___________
164.  I take responsibility for my decisions because ___________
165.  When I make a wrong decision, I ___________
166.  Important decisions should be ___________
167.  I am confident in my decisions when ___________
168.  Before deciding, I ___________
169.  Under time pressure, I decide by ___________
170.  I learn from bad decisions by ___________
WOMEN & GENDER
171.  Women in the military ___________
172.  I believe women should ___________
173.  The role of women in society is ___________
174.  Female officers in Pakistan Army ___________
175.  Gender equality means ___________
RELIGION & SPIRITUALITY
176.  My religion teaches me ___________
177.  Faith helps me ___________
178.  I believe God ___________
179.  Religious values are ___________
180.  Spirituality in life means ___________
PAKISTAN & PATRIOTISM
181.  Pakistan is ___________
182.  I am proud of Pakistan because ___________
183.  Pakistan's future ___________
184.  A good Pakistani citizen should ___________
185.  Pakistan's biggest challenge is ___________
186.  I can serve Pakistan by ___________
187.  Pakistan's strength lies in ___________
188.  Love for Pakistan means ___________
189.  Pakistan was made for ___________
190.  My duty to Pakistan is ___________
LIFE PHILOSOPHY
191.  Life to me is ___________
192.  I live life by ___________
193.  The meaning of life is ___________
194.  My philosophy of life is ___________
195.  I believe that every person should ___________
196.  Life teaches me ___________
197.  Living with purpose means ___________
198.  I believe happiness comes from ___________
199.  The lesson life has taught me is ___________
200.  I face life's challenges by ___________
GENERAL / MISCELLANEOUS
201.  I enjoy ___________
202.  I hate ___________
203.  My hobbies include ___________
204.  In my free time, I ___________
205.  My greatest achievement so far is ___________
206.  My greatest regret is ___________
207.  I am curious about ___________
208.  I laugh when ___________
209.  Traveling makes me ___________
210.  I read books about ___________
RELATIONSHIPS WITH OTHERS
211.  I find it easy to ___________
212.  I find it hard to ___________
213.  Most people I know are ___________
214.  I treat others with ___________
215.  I believe people are ___________
216.  I help others because ___________
217.  I become close to people who ___________
218.  I keep my distance from people who ___________
219.  I show respect to ___________
220.  I admire people who ___________
FUTURE & CAREER
221.  My career goal is ___________
222.  I see myself in 5 years as ___________
223.  If I do not join the army, I will ___________
224.  My ideal profession is ___________
225.  The career that suits me best is ___________
226.  After retirement, I want to ___________
227.  Professional growth for me means ___________
228.  I want to leave behind ___________
229.  My long-term career plan is ___________
230.  Service to others in my career means ___________
NATURE & ADVENTURE
231.  Nature makes me feel ___________
232.  I feel at peace when ___________
233.  The outdoors ___________
234.  I find nature ___________
235.  Adventure for me means ___________
CONFLICT & DIFFICULT SITUATIONS
236.  When someone is rude to me, I ___________
237.  When I disagree with my superior, I ___________
238.  I handle conflict by ___________
239.  Arguments make me ___________
240.  When someone betrays my trust, I ___________
RESPONSIBILITY & ACCOUNTABILITY
241.  Responsibility means ___________
242.  I take responsibility for ___________
243.  When I make a mistake, I ___________
244.  Accountability for me means ___________
245.  I feel most responsible when ___________
FINAL REFLECTIONS
246.  Sacrifice means ___________
247.  Hard work for me means ___________
248.  Time management is ___________
249.  A challenge I want to overcome is ___________
250.  My message to myself is ___________
1. I am satisfied....................................................................................
2. He failed in........................................................................................
3. We reached the station..................................................................
4. Old habits are...................................................................................
5. You cannot succeed.........................................................................
6. He has broken...................................................................................
7. The way is long but..........................................................................
8. He supported....................................................................................
9. He did everything.............................................................................
10. Follow the man..............................................................................
11. Drinking and smoking...................................................................
12. One should adhere........................................................................
13. His greater fear is...........................................................................
14. You should take advantage..........................................................
15. The women should........................................................................
16. An intelligent..................................................................................
17. Go ahead with................................................................................
18. Time blunts.....................................................................................
19. He devoted his...............................................................................
20. Let us discuss..................................................................................
21. His negligence.................................................................................
22. Love is..............................................................................................
23. Indian agents..................................................................................
24. It is no use.......................................................................................
25. A Teacher's duty............................................................................
26. The weather is bad but.................................................................
27. Get up and......................................................................................
28. My greatest wish............................................................................
29. Struggle for.....................................................................................
30. A man may learn............................................................................
31. Our characters are.........................................................................
32. In order to learn.............................................................................
33. Truth site upon...............................................................................
34. The man of culture........................................................................
35. The memories of childhood.........................................................
36. I wish I could...................................................................................
37. She is angry because.....................................................................
38. Hope is a good................................................................................
39. All rising to great place..................................................................
40. A statesman should.......................................................................
41. Nothing is more unpleasant.........................................................
42. Let us find........................................................................................
43. Money speaks sense......................................................................
44. When faced with a difficult problem..........................................
45. The new generation......................................................................
46. My principle is................................................................................
47. Have faith in....................................................................................
48. Among new problem.....................................................................
49. Nation should not..........................................................................
50. Keep yourself..................................................................................
51. Garden is.........................................................................................
52. Pakistan is now..............................................................................
53. Grapple with...................................................................................
54. Life is the art of..............................................................................
55. March with.....................................................................................
56. The history of art...........................................................................
57. Get up early and............................................................................
58. In the darkness...............................................................................
59. I feel I am........................................................................................
60. I like movies about.........................................................................
61. On the frontline..............................................................................
62. I shall always...................................................................................
63. Our army needs..............................................................................
64. I do not want..................................................................................
65. In all my life.....................................................................................
66. Do you think...................................................................................
67. I dream about.................................................................................
68. When I got tired.............................................................................
69. If someone disturb me..................................................................
70. All great people..............................................................................
71. I usually go......................................................................................
72. Our flag...........................................................................................
73. He expects your..............................................................................
74. Our shaheeds..................................................................................
75. When I am alone............................................................................
76. After the death of..........................................................................
77. Do something by and by...............................................................
78. A commando..................................................................................
79. I am ready to..................................................................................
80. These steps will clear.....................................................................
81. Many young persons.....................................................................
82. I can assure you..............................................................................
83. Enjoy................................................................................................
84. The red colour................................................................................
85. His father.........................................................................................
86. Do away with..................................................................................
87. You should be.................................................................................
88. Our forces.......................................................................................
89. His hobbies are...............................................................................
90. I appreciate.....................................................................................
91. We are in defense of.....................................................................
92. Whenever I go there.....................................................................
93. An honourable man.......................................................................
94. At the discretion of........................................................................
95. Try your best...................................................................................
96. When working together................................................................
97. Lend me your ears and..................................................................
98. The TV plays....................................................................................
99. Good health....................................................................................
100. Do not speak next........................................................................ 
1. On his Youth, Ahmad wanted to...
2. She was all alone If I had a gun ...
3. Generally illness...
4. There is a limit to...
5. Evil spirits...
6. I seldom...
7. At night...
8. The fight...
9. The only way left...
10. She wants him....
11. In my opinion....
12. We have to tolerate....
13. When war was on ...
14. He is troubled by....
15. They are usually...
16. I am not aware that...
17. When she grew old...
18. Far away from his house...
19. It us very seldom that he...
20. If it is necessary I will...
21. To gain portion of his time...
22. The teacher feels...
23. He was hopeful...
24. Our leaders are....
25. He wants to win...
26. It is very seldom that he 	
27. To express his anger	
28. It was very clear that	
29. Because of a little discomfort	
30. To gain popularity he	
31. He possesses
32. To avoid failure he
33. I am not aware that	
34. when she grew old	
35. he became impatient when	
36. In a fit of rage he	
37. It is quite Natural that girl	
38. If u insult him	
39. It was obvious that	
40. On seeing the blood he	
41. I always feel...
42. I m interested in...
43. His mind is...
44. I dislike...
45. In a short time...
46. He wants to...
47. He offered me...
48. He never used...
49. I never...
50. I cannot tolerate...
51. I lack...
52. I need...
53. I am ashamed when...
54. After his failure...
55. In alone time me...
56. Girls are...
57. Girl's legs are...
58. I love...
59. I am not afraid of...
60. Life has...
61. I am surprise...
62. He wanted...
63. To become rich...
64. He could not...
65. Hard ship...
66. When he was alone...
67. He is upset...
68. Money is ...
69. He tried...
70. My greatness weakness is...
71. My sex relation...
72. He needs...
73. I love...
74. My ambition...
75. A time will come...
76. My father...
77. My school...
78. A brother...
79. The boy and girl...
80. Keep your...
81. Every young man...
82. After great effort...
83. My sister was...
84. In simple world...
85. I have never done...
86. Until you apologized...
87. It's fashionable now....
88. I am having trouble...
89. He felt ashamed of...
90. His share of....
91. Music is...
92. He spread the rumor that...
93. It is high time that...
94. Our leaders are...
95. To express his anger...
96. It us very seldom that he...
97. He became impatient when he...
98. Far away from his house...
99. When she grew old....
100. He is always willing to...
101. I am not aware..."""

sct_urd_text = """میں زندگی میں سب سے زیادہ ـــــــ چاہتا ہوں۔
میری سب سے بڑی کمزوری ـــــــ ہے۔
میں جب اکیلا ہوتا ہوں تو ـــــــ۔
میرے والدین چاہتے ہیں کہ میں ـــــــ۔
میری زندگی کا مقصد ـــــــ ہے۔
مجھے سب سے زیادہ خوشی ـــــــ سے ملتی ہے۔
میں فوج میں اس لیے جانا چاہتا ہوں کیونکہ ـــــــ۔
میرے دوست مجھے ـــــــ سمجھتے ہیں۔
جب مجھ پر ذمہ داری آتی ہے تو میں ـــــــ۔
میری سب سے بڑی خوبی ـــــــ ہے۔
ناکامی کے وقت میں ـــــــ۔
میں اپنے آپ کو ـــــــ سمجھتا ہوں۔
میرا آدرش ـــــــ ہے۔
مشکل حالات میں میں ـــــــ۔
میری پسندیدہ کتاب ـــــــ ہے۔
میں اپنے ملک کے لیے ـــــــ کرنا چاہتا ہوں۔
میری ماں ـــــــ ہے۔
میرے باپ نے مجھے سکھایا کہ ـــــــ۔
میں جب غصے میں ہوتا ہوں تو ـــــــ۔
میری سب سے بڑی خواہش ـــــــ ہے۔
میں نے زندگی میں سب سے بڑی غلطی ـــــــ کی۔
میں اپنے گروپ میں ـــــــ کردار ادا کرتا ہوں۔
دوسروں کی مدد کرنا مجھے ـــــــ لگتا ہے۔
میں نے آج تک سب سے مشکل کام ـــــــ کیا۔
میرے استاد نے مجھے بتایا کہ ـــــــ۔
میں اپنے بھائیوں کے ساتھ ـــــــ۔
میرے نزدیک کامیابی کا مطلب ـــــــ ہے۔
میں اپنی غلطی پر ـــــــ۔
میرے نزدیک ایک اچھا لیڈر وہ ہے جو ـــــــ۔
میں مستقبل میں ـــــــ بننا چاہتا ہوں۔
جب کوئی مجھ سے اختلاف کرے تو میں ـــــــ۔
میری زندگی کی سب سے بڑی کامیابی ـــــــ ہے۔
میں اپنی ٹیم کے لیے ـــــــ کرتا ہوں۔
میرے نزدیک وطن کی خدمت ـــــــ ہے۔
جب کوئی مصیبت آتی ہے تو میں ـــــــ۔
میں اپنے ساتھیوں سے ـــــــ توقع رکھتا ہوں۔
میری زندگی میں سب سے اہم شخص ـــــــ ہے۔
مجھے سب سے زیادہ تکلیف ـــــــ سے ہوتی ہے۔
میں ہمیشہ ـــــــ پر یقین رکھتا ہوں۔
میری کمزوری یہ ہے کہ میں ـــــــ۔
میں نے اپنی زندگی میں ـــــــ سے سبق سیکھا۔
جب مجھے تنقید کی جاتی ہے تو میں ـــــــ۔
میں اپنی ذمہ داریوں کو ـــــــ سمجھتا ہوں۔
میرے نزدیک دوستی کا مطلب ـــــــ ہے۔
میں دباؤ میں ـــــــ۔
میں اپنے مستقبل کے بارے میں ـــــــ سوچتا ہوں۔
میری سب سے بری عادت ـــــــ ہے۔
میں گروپ میں کام کرتے وقت ـــــــ۔
جب میں تھکا ہوا ہوتا ہوں تو ـــــــ۔
مجھے فخر ہے کہ میں ـــــــ۔
میں نے پاک فوج کو اس لیے چنا کیونکہ ـــــــ۔
میرے نزدیک قربانی کا مطلب ـــــــ ہے۔
میں اپنے آپ کو بہتر بنانے کے لیے ـــــــ کرتا ہوں۔
مجھے سب سے زیادہ ڈر ـــــــ سے لگتا ہے۔
میں اپنے فیصلے ـــــــ طریقے سے کرتا ہوں۔
میرے نزدیک نظم و ضبط ـــــــ ہے۔
میں اپنے جونیئرز کے ساتھ ـــــــ۔
میری پسندیدہ شخصیت ـــــــ ہے۔
جب کوئی میری مدد نہ کرے تو میں ـــــــ۔
میں نے کبھی ـــــــ نہیں کیا۔
میرے نزدیک ایمانداری ـــــــ ہے۔
میں ہر روز ـــــــ کرتا ہوں۔
میری پسندیدہ کھیل ـــــــ ہے۔
جب مجھے غلط کہا جائے تو میں ـــــــ۔
میں اپنے گھر میں ـــــــ کردار ادا کرتا ہوں۔
مجھے سب سے زیادہ پریشانی ـــــــ سے ہوتی ہے۔
میں نے زندگی میں سب سے بڑا سبق ـــــــ سے سیکھا۔
میں اپنے دشمن کے ساتھ ـــــــ۔
میرے نزدیک اچھا انسان وہ ہے جو ـــــــ۔
میں اپنی ناکامی کا ذمہ دار ـــــــ کو سمجھتا ہوں۔
میری خواہش ہے کہ میرا ملک ـــــــ۔
میں مشکل کام کو ـــــــ طریقے سے کرتا ہوں۔
میرے نزدیک جھوٹ ـــــــ ہے۔
میں اپنے سینیئرز کی ـــــــ کرتا ہوں۔
میری زندگی کا سب سے خوشگوار لمحہ ـــــــ تھا۔
میں اپنی ٹیم کو ـــــــ طرح متحرک کرتا ہوں۔
مجھے اپنی زندگی میں سب سے زیادہ پچھتاوا ـــــــ پر ہے۔
میں اپنے آپ کو لیڈر اس لیے سمجھتا ہوں کیونکہ ـــــــ۔
جب کوئی میرے فیصلے سے اتفاق نہ کرے تو میں ـــــــ۔
میرے نزدیک پاکستان کا سب سے بڑا مسئلہ ـــــــ ہے۔
میں اپنی صلاحیتوں کو ـــــــ کام میں استعمال کرتا ہوں۔
میرے نزدیک ایک اچھے افسر کی سب سے بڑی خوبی ـــــــ ہے۔
جب مجھے کوئی آرڈر دیا جائے تو میں ـــــــ۔
میں اپنی ذاتی مشکلات کو ـــــــ طریقے سے حل کرتا ہوں۔
میں نے اپنی زندگی کا سب سے بہادرانہ کام ـــــــ کیا۔
میں اپنے دوستوں کو ـــــــ اہمیت دیتا ہوں۔
میرے نزدیک وقت کی پابندی ـــــــ ہے۔
میں فارغ وقت میں ـــــــ کرتا ہوں۔
میری پسندیدہ فوجی شخصیت ـــــــ ہے۔
میں ہمیشہ اپنی بات ـــــــ طریقے سے کہتا ہوں۔
جب کوئی میرا حق مارے تو میں ـــــــ۔
میرے نزدیک شہادت ـــــــ ہے۔
میں خطرے کے وقت ـــــــ۔
میری سوچ یہ ہے کہ پاکستان کو ـــــــ کی ضرورت ہے۔
مجھے فوجی زندگی میں سب سے زیادہ ـــــــ پسند ہے۔
میں اپنے مخالف کو ـــــــ نظر سے دیکھتا ہوں۔
میرے نزدیک قوم پرستی کا مطلب ـــــــ ہے۔
جب مجھ پر اعتماد کیا جائے تو میں ـــــــ۔
میری سب سے بڑی ترجیح ـــــــ ہے۔
میں دوسروں کی رائے کو ـــــــ سمجھتا ہوں۔
میرے نزدیک ایک کامیاب زندگی وہ ہے جس میں ـــــــ۔
میں اپنے ملک کی خدمت ـــــــ طریقے سے کرنا چاہتا ہوں۔
میرے نزدیک خود اعتمادی ـــــــ ہے۔
جب میری ٹیم ہار جائے تو میں ـــــــ۔
میں نے کبھی ـــــــ کا سامنا کیا۔
میں اپنی ماں کو ـــــــ سمجھتا ہوں۔
میرے نزدیک محنت ـــــــ ہے۔
جب کوئی میرے ساتھ بے انصافی کرے تو میں ـــــــ۔
میں اپنی غلطیوں سے ـــــــ سیکھتا ہوں۔
میری زندگی میں سب سے مشکل فیصلہ ـــــــ تھا۔
میں اپنے آپ کو ـــــــ ثابت کرنا چاہتا ہوں۔
میرے نزدیک دشمن کا مقابلہ ـــــــ سے کرنا چاہیے۔
جب میرے پاس وسائل کم ہوں تو میں ـــــــ۔
میں اپنی کامیابی کا سہرا ـــــــ کو دیتا ہوں۔
میرے نزدیک پاکستان کا روشن مستقبل ـــــــ میں ہے۔
میں اپنی ٹیم کے کمزور ساتھی کو ـــــــ۔
مجھے سب سے زیادہ ـــــــ کی فکر رہتی ہے۔
میرے نزدیک بہترین سپاہی وہ ہے جو ـــــــ۔
جب میں غلطی کروں تو میں ـــــــ۔
میں اپنی کمزوریوں کو ـــــــ طریقے سے دور کرتا ہوں۔
میری زندگی کا سب سے مشکل دور ـــــــ تھا۔
میں اپنی جیت کو ـــــــ کے ساتھ مناتا ہوں۔
میرے نزدیک جرأت کا مطلب ـــــــ ہے۔
جب میں کسی نئی جگہ جاتا ہوں تو ـــــــ۔
میں اپنی بات ـــــــ انداز میں کہتا ہوں۔
میرے نزدیک ٹیم ورک ـــــــ ہے۔
مجھے سب سے زیادہ خوف ـــــــ سے ہوتا ہے۔
میں اپنے مقصد کے لیے ـــــــ قربان کر سکتا ہوں۔
جب مجھے کوئی ناسمجھ کہے تو میں ـــــــ۔
میری زندگی کا سب سے یادگار سفر ـــــــ تھا۔
میں اپنے آپ کو جسمانی طور پر ـــــــ رکھتا ہوں۔
میرے نزدیک ایک برے افسر کی سب سے بڑی کمزوری ـــــــ ہے۔
جب مجھے کوئی حکم دے جو غلط लगे تو میں ـــــــ۔
میں اپنی ذاتی زندگی کو ـــــــ طریقے سے گزارتا ہوں۔
میرے نزدیک ملک کی سالمیت ـــــــ سے زیادہ اہم ہے۔
جب میری ٹیم میں اختلاف ہو تو میں ـــــــ۔
میں نے اپنی زندگی میں سب سے زیادہ ـــــــ سے محبت کی۔
میرے نزدیک ایک اچھا دوست وہ ہے جو ـــــــ۔
میں اپنے مستقبل کے لیے ـــــــ منصوبہ بندی کرتا ہوں۔
جب سب مجھ سے مخالفت کریں تو میں ـــــــ۔
میں اپنے وطن کے لیے ـــــــ تک لڑ سکتا ہوں۔
میرے نزدیک تعلیم کا مقصد ـــــــ ہے۔
جب میں ناکام ہوتا ہوں تو میں ـــــــ سوچتا ہوں۔
میری سب سے بڑی خوشی ـــــــ کو خوش دیکھنا ہے۔
میں خود کو ہر حال میں ـــــــ رکھتا ہوں۔
میرے نزدیک جنگ آخری حل ـــــــ ہے۔
میں اپنے گروپ کی قیادت ـــــــ طریقے سے کرتا ہوں۔
مجھے سب سے زیادہ تسلی ـــــــ سے ملتی ہے۔
جب مجھے کوئی دھوکہ دے تو میں ـــــــ۔
میرے نزدیک پاک فوج ـــــــ ہے۔
میں اپنی بہن کو ـــــــ سمجھتا ہوں۔
میری ناکامی کی سب سے بڑی وجہ ـــــــ ہے۔
میں مستقبل میں اپنے ملک کو ـــــــ دیکھنا چاہتا ہوں۔
میرے نزدیک صبر ـــــــ ہے۔
جب کوئی میری مدد مانگے تو میں ـــــــ۔
میں اپنے آپ کو بہتر ثابت کرنے کے لیے ـــــــ کرتا ہوں۔
میرے نزدیک خاندان ـــــــ ہے۔
جب میں خوش ہوتا ہوں تو ـــــــ۔
میری سب سے بری یاد ـــــــ ہے۔
میں اپنے ملک کے دشمنوں کو ـــــــ سمجھتا ہوں۔
میں مشکل میں ـــــــ کی مدد لیتا ہوں۔
میرے نزدیک اللہ پر بھروسہ ـــــــ ہے۔
جب کام کا بوجھ زیادہ ہو تو میں ـــــــ۔
میری پسندیدہ چیز ـــــــ ہے۔
میں اپنی زندگی کو ـــــــ بنانا چاہتا ہوں۔
میرے نزدیک قائداعظم کا سب سے بڑا کارنامہ ـــــــ ہے۔
جب کوئی میرے قریبی کو تکلیف دے تو میں ـــــــ۔
میں اپنی صحت کا خیال ـــــــ طریقے سے رکھتا ہوں۔
میرے نزدیک سب سے بڑی دولت ـــــــ ہے۔
جب میں کوئی غلط کام دیکھوں تو میں ـــــــ۔
میرے نزدیک جوانی کا سب سے بڑا فریضہ ـــــــ ہے۔
میں اپنی ناکامی کو ـــــــ کے طور پر لیتا ہوں۔
جب مجھے تنہا کام کرنا پڑے تو میں ـــــــ۔
میرے نزدیک قوم کی ترقی ـــــــ سے ممکن ہے۔
میں اپنے کردار کو ـــــــ بنانا چاہتا ہوں۔
جب میرے اوپر ناانصافی ہو تو میں ـــــــ۔
میرے نزدیک سب سے بڑا ہتھیار ـــــــ ہے۔
میں اپنی ذات کو قوم کے لیے ـــــــ کرنا چاہتا ہوں۔
جب کوئی میری کامیابی سے جلے تو میں ـــــــ۔
میرے نزدیک زندگی کا سب سے قیمتی لمحہ ـــــــ ہے۔
میں اپنے اردگرد کے لوگوں کو ـــــــ نظر سے دیکھتا ہوں۔
میرے نزدیک اتحاد ـــــــ ہے۔
جب میں کوئی بڑا فیصلہ کروں تو ـــــــ۔
میں اپنی پوری زندگی ـــــــ کے اصولوں پر چلنا چاہتا ہوں۔
میرے نزدیک سب سے بڑا گناہ ـــــــ ہے۔
جب میرا دوست غلطی کرے تو میں ـــــــ۔
میں اپنی ذہنی صلاحیتوں کو ـــــــ کام میں لاتا ہوں۔
میرے نزدیک فتح کا راستہ ـــــــ سے گزرتا ہے۔
جب مجھے کوئی چیلنج ملے تو میں ـــــــ۔
میں اپنی کامیابی کو ـــــــ تک محدود نہیں رکھتا۔
میرے نزدیک علامہ اقبال کا سب سے بڑا پیغام ـــــــ ہے۔
جب میں کوئی ہدف مقرر کروں تو ـــــــ۔
میں اپنے ساتھیوں کی کمزوریوں کو ـــــــ سمجھتا ہوں۔
میرے نزدیک سب سے بڑی طاقت ـــــــ ہے۔
جب میں کوئی نئی ذمہ داری لوں تو ـــــــ۔
میں اپنے ملک کی تاریخ کو ـــــــ سمجھتا ہوں۔
میرے نزدیک ایک سچا مسلمان ـــــــ ہوتا ہے۔
جب میں اپنا ہدف حاصل کر لوں تو ـــــــ۔
میں اپنی زندگی میں آنے والی مشکلات کو ـــــــ سمجھتا ہوں۔
میرے نزدیک پاکستان زندہ باد کا مطلب ـــــــ ہے۔
میں ہر حال میں ـــــــ کے ساتھ کھڑا رہتا ہوں۔
میرے نزدیک سب سے بڑی عبادت ـــــــ ہے۔
جب میں اپنے گھر سے دور ہوں تو ـــــــ۔
میں اپنے جوش کو ـــــــ طریقے سے استعمال کرتا ہوں۔
میرے نزدیک آزادی کی قدر ـــــــ کو پتا ہوتی ہے۔
جب کوئی میرے ملک کو برا کہے تو میں ـــــــ۔
میں اپنے خوابوں کو ـــــــ بنانا چاہتا ہوں۔
میرے نزدیک سب سے بڑی سزا ـــــــ ہے۔
جب میں تھکا ہوا ہوں پھر بھی ـــــــ۔
میری زندگی کا سب سے بڑا محرک ـــــــ ہے۔
میں اپنی غلطی کا اعتراف ـــــــ کے سامنے کرتا ہوں۔
میرے نزدیک خوف ـــــــ ہے۔
جب سب ہمت ہار لیں تو میں ـــــــ۔
میں اپنی قوم کے لیے ـــــــ بننا چاہتا ہوں۔
میرے نزدیک پاکستان کی سب سے بڑی طاقت ـــــــ ہے۔
جب مجھے کوئی اکیلا چھوڑ دے تو میں ـــــــ۔
میں اپنی زندگی میں ـــــــ کو سب سے زیادہ یاد کرتا ہوں۔
میرے نزدیک ایک سچا دیش بھگت ـــــــ ہوتا ہے۔
جب مجھے کسی مشکل مشن پر بھیجا جائے تو ـــــــ۔
میری نظر میں سب سے بڑا انسان وہ ہے جو ـــــــ۔
میں اپنے افسر کی ہر بات ـــــــ۔
میرے نزدیک موت سے ڈرنا ـــــــ ہے۔
جب میرے سامنے دو راستے ہوں تو میں ـــــــ۔
میں نے اپنی زندگی میں سب سے زیادہ ـــــــ سے محنت کی۔
میرے نزدیک پاکستان کا دفاع ـــــــ کی ذمہ داری ہے۔
جب میں میدان جنگ میں ہوں تو ـــــــ۔
میں اپنے گھر والوں کو ـــــــ کے ساتھ یاد کرتا ہوں۔
میرے نزدیک قیادت ـــــــ کا نام ہے۔
جب کوئی کمزور مجھ سے مدد مانگے تو میں ـــــــ۔
میری سوچ کے مطابق آج کے نوجوان کو ـــــــ چاہیے۔
میں اپنے سامنے آنے والی ہر رکاوٹ کو ـــــــ سمجھتا ہوں۔
میرے نزدیک اخلاق ـــــــ ہے۔
جب میرے ملک کو خطرہ ہو تو میں ـــــــ۔
میں اپنے آپ پر ـــــــ کی وجہ سے فخر کرتا ہوں۔
میرے نزدیک زندگی کا سب سے بڑا امتحان ـــــــ ہے۔
جب کوئی میری محنت کو نظرانداز کرے تو میں ـــــــ۔
میں اپنی قوم کی ترقی کے لیے ـــــــ کرنے کو تیار ہوں۔
میرے نزدیک سب سے بڑی کمزوری ـــــــ ہے۔
جب میں آئینے میں دیکھتا ہوں تو ـــــــ نظر آتا ہے۔
میری سب سے بڑی دعا یہ ہے کہ ـــــــ۔
میں اپنے ہر کام میں ـــــــ کو مدنظر رکھتا ہوں۔
میرے نزدیک مایوسی ـــــــ ہے۔
جب سب لوگ میرے خلاف ہوں تو میں ـــــــ۔
میں اپنے آپ کو روزانہ ـــــــ کے ذریعے بہتر کرتا ہوں۔
میرے نزدیک پاکستانی ہونا ـــــــ ہے۔
جب مجھے کوئی بڑا موقع ملے تو میں ـــــــ۔
میں اپنی زندگی کے ہر لمحے کو ـــــــ سمجھتا ہوں۔
میرے نزدیک سب سے بڑی دولت ـــــــ ہے۔
جب میں فوجی وردی پہنوں گا تو ـــــــ۔
میں پاکستان زندہ باد کہتا ہوں کیونکہ ـــــــ۔"""

pointer_text = """Their relations were very good but suddenly…
She was all alone in her room suddenly…
Her life was glamour’s till…
The relation took new turn when…
He could not stand firm because…
Ali was sitting with his friends suddenly…
He was unable to bear the expenses of his family than he…
In a dark stormy night she was all alone in her home suddenly…
He joined services to earn money but when he becomes leader of man…
He was very hard worker but fail to fulfill his expenses so he…
She was standing on a lonely road suddenly her…
He wanted to become a rich man but when he becomes a leader of men he…
AMJAD feels his youth and he wants to provide of…
He decides to join Army for money but…
Zahoor was poor boy one day he…
Their relation take a new turn when…
Friends were sitting in around suddenly…
When he saw her in trouble than he…
They were friends and were sitting together but suddenly…
On seeing a lonely girl on the road, he…
He worked very hard but…
The Enemy was Strong but…
He could not afford his family expenditure then he decided…
He was very hard worker but failed to fulfill his expenses so he…
He decided to join Army for money but…
He could not stand firm because…
In a lust of money & power he…
Lust of money and power made him…
He worked hard day and night but could not meet the expense of his family so he decided to…
One thunderstorm night, she was all alone on the road but suddenly…
Maira was all alone in her room at midnight that suddenly…
Amna's life was full of joy and glamour till…
Despite having got rid of police, he could not stand firm because…
Ali was sitting with his female class fellow in the university cafe that…
He was doing job during day and tuition in the evening yet was unable to bear the expenses of his family, so he…"""

wat_text = """Accept
Work
Atom
Country
Army
Step
Company
Love
Duty
Girl
Fat
Decide
Beat
Fight
Lie
Give
Enjoy
Bright
Careful
Success
Trust
Solve
Story
Break
Fear
Defeat
Attack
Home
Afraid
Able
Excuse
Luck
Good
Knife
Encourage
Danger
Family
Bad
Office
Agree
Sad
Soldier
Assist
Regarded
Cannot
Drink
Begin
Holiday
Discipline
Girl
Playground
Fellow
Dictatorship
Fellow
Attack
Risk
Award
Withdraw
Defeat
Snake
Continue
Custom
Music
Enjoy
Army
Enemy
Garden
Faith
Help
Cinema
Money
Peace
Fine
Delay
Character
Travel
Journey
Ghost
Respect
Duty
Life
Poor
Use
Climb
Problem
Attempt
Happy
Book
Rest
Short
Design
Save
Sick
War
Alone
Father
System
Make
Nature
Difficulty
Health
Impossible
Lonely
Affection
Sympathy
Company
Courage
Meet
Secure
Responsibility
Love
Character
Understanding
Sport
Responsible
Tried
Boat
Duty
Fail
Action
Fight
Problem
Friend
Risk
Struggle
Achieve
Worry
Furniture
Fault
Co-operation
Discipline
Plane
Neglect
Step
Climb
Life
Will
Honesty
Machine
Afraid
Lead
Think
Hobby
Obtain
Idea
Solve
Afraid
Religion
Morality
Innovation
Trust
Attack
Continuous
Punctuality
Failure
Science
Space
Sky
Goal
Busy
Mother
Save
Urge
FALSE
Knowledge
Sleep
Unfair
Sister
Beat
Cannot
Project
Regular
Adventure
Climb
Fly
Now
Tie
Slow
Light
Pressure
Dig
Sink
Contract
Rear
Real
Fact
Pay
Cash
Cost
Believe
Luck
Look
Think
Fortune
Think
Protect
Task
Slip
Drop
Snake
Award
Achieve
Assist
Action
Agree
Avoid
Alone
Ambition
Attempt
Attack
Appeal
Air
Arrived
Accept
Bad
Blood
Book
Beautiful
Cut
Copy
Co-operation
Change
Chance
Challenge
Coward
Decide
Rest
Alone
Avoid
Shine
Rumor
Careful
Defense
Confidence
Serious
Revenge
Atom
Humble
Talk
Natural
Take
Easy
Shock
Prepare
Greed
Time
Scene
Drive
Tackle
Wait
Dangerous
Study
Accept
Plan
Difficulties
Jump
Differ
Protect
Hate
Use
Help
Interest
Society
Careful
Fast
Train
Reaction
Group
Health
Blood
Fortune
Merry
Loyalty
Ask
Disagree
Prejudice
Misfortune
Fortune
Choose
Genuine
Pick
Impossible
Efficiency
Attack
Enemy
Childhood
Challenge
Find
Action
Sympathy
Beauty
Cinema
Think
Nature
Change
Money
Death
Brace
War
Pity
Victory
Trial
Sick
Single
Travel
Jump
Joy
Help
Quick
Step
Rule
Reframe
Stop
Pleasure
Team
Soldier
Alone
Struggle
Gallant
Insist
Life
Worry
Provide
Relax
Society
Loyal
Love
Punish
Resist
Success
Regret
Haste
Responsible
Withdraw
Use
Zeal
Yield
Support
Insist
Make
Luck
Future
Progress
Possible
Question
Solve
Since
Truth
Leader
Injustice
Failure
Gay
Happy
Guide
Honest
Impossible
Lose
Sacrifice
Simple
Secret
Quit
Rent
Rigid
Serious
Peace
Meet
Risk
Sad
Sister
Religion
Sensible
Lonely
Lead
Protect
Plane
Atom
Character
Difficulty
Ghost
Good
Fir
Heart
Patience
Home
Need
Work
Flower
Chair
Power
Sword
Interview
Adversity
Tried
Morality
Problem
Persuade
Service
Think
Wisdom
Influence
Suicide
Strength
Security
Time
Uppermost
Wife
Weak
Contact
Escape
Efficiency
Annoy
Fear
Risk
Mountain
Leaf
Wine
Win
Music
Flag
Bad
Foreign
Young
Play
Offer
Well
Difficult
Success
Curious
Appeal
Fire
Reform
Assist
Mistake
Mother
Overcome
Complex
Confuse
Hasty
Hope
Danger
Precaution
Fever
Fellow
Strict
Hesitate
Girl
Field
Trouble
Compel
Smoke
Firing
Patriot
Death
Stop
Run
Book
Find
Differ
Light
Admire
Advice
Coward
Drink
Shoot
Puzzle
Speak
Unable
Child
Criticize
Character
Company
Religion
Persist
Keen
Organize
Progress
Arrange
Football
Playground
Decide
Confuse
Persuade
Defend
Lovely
Begin
Adopt
Dislike
Believe
Displeasure
Sputnik
Insist
Respect
Service
Faith
Absolute
Kill
Cautions
Climb
Compel
Complete
Initiative
Future
Circumstance
Ahead
Ambition
Bold
Difficult
Friend
Follow
Differ
Confuse
Attempt
Dislike
Affection
Character
Co-operative
Defense
Fair
Machine"""

srts_text = """1
You have received your call for ISSB and are to travel by train. On reaching the railway station you find that the train you wanted to catch is just starting and there is hardly any time to purchase the ticket. What will you do?
2
You want to join Army but due to various reasons you applied late and your age is about to exceed the limit. During the initial test you find the academic paper too tough. What will you do?
3
You are in the parking area of a shopping complex. Suddenly electricity fails and there is total darkness. What will you do?
4
You got admission in a college in another city and your parents decide you will stay in hostel. When you join hostel you find your roommate is not friendly. What will you do?
5
You and your friends planned a picnic. On the way a heated discussion starts between you and your friends which spoils your mood. What will you do?
6
You did well in FSC exam and got a government prize of Rs 500,000. How will you spend this amount?
7
A wave of COVID-19 spreads in your village and people start leaving their houses. What will you do?
8
While studying late at night you see four masked men entering your neighbour’s house saying they will finish in 15 minutes. What will you do?
9
You are an Army officer and one of your soldiers asks for leave saying his mother is sick but you suspect he might be lying. What will you do?
10
You are a doctor fasting in Ramazan and about to leave for iftar when a seriously injured person is brought to the clinic. What will you do?
11
While travelling to ISSB you reach Lahore and realize that you have lost your purse and you know nobody there. What will you do?
12
You have poor academic results and little chance of university admission. What will be your next step?
13
You learn that your elder brother has been arrested for murder and he admits the crime. What will you do?
14
You received ISSB call but your father gets a heart attack a night before departure. What will you do?
15
While watching a movie in a cinema hall you suddenly notice a snake near your feet. What will you do?
16
While returning from a friend’s farmhouse late at night you lose your way and your phone is not working. What will you do?
17
Your boss gives an order but you feel his instructions are wrong and harmful. What will you do?
18
You are driving a car on the highway and suddenly the brakes fail. What will you do?
19
Electricity in your colony suddenly goes off due to storm. What will you do?
20
You are travelling by train and lose your purse with money. What will you do?
21
You are travelling by bus and suddenly the engine catches fire. What will you do?
22
Your boss assigns a task that seems impossible to finish in given time. What will you do?
23
You bought a watch from a smuggled goods seller but it is not working. What will you do?
24
Your team captain is injured before an important match and you are asked to lead the team. What will you do?
25
Your brother wants admission in medical college but falls short by 1%. What will you do?
26
You have to travel with cash to a dangerous area where dacoits operate. What will you do?
27
While travelling by train a thief snatches a purse from a woman and jumps out. What will you do?
28
You are about to sign an important contract when you hear your friend met an accident and is in ICU. What will you do?
29
You boarded the wrong train and realize when the ticket checker asks for ticket. What will you do?
30
You see your girlfriend walking with another person in a park. What will you do?
31
While going to railway station a car throws a person out of the moving vehicle. What will you do?
32
You are driving a bike without helmet and traffic police stops you. What will you do?
33
Two days before a badminton tournament your partner leaves the city. What will you do?
34
While walking with your sister at night a group of men starts harassing her and police station is far away. What will you do?
35
You see a snake moving near your younger brother who is sleeping. What will you do?
36
You receive an order from commander but feel the order is wrong. What will you do?
37
During exam teacher asks you to help another student cheat and threatens to fail you if you refuse. What will you do?
38
Your parents want you to marry a rich girl but you love someone else. What will you do?
39
During exam you see your best friend copying from a book. What will you do?
40
While travelling in desert you see a seriously injured person with no one around. What will you do?
41
While travelling to ISSB you lose your suitcase containing documents. What will you do?
42
On the day of leaving for ISSB your brother dies due to heart attack. What will you do?
43
You oppose a student strike and your classmates beat you. What will you do?
44
You argued with your friend but later realize he was right. What will you do?
45
You want to study but friends keep disturbing you. What will you do?
46
A criminal snatches a gold chain from a woman and you are the only person nearby. What will you do?
47
You are invited to dinner by a friend but must also attend company dinner the same day. What will you do?
48
You are studying engineering but feel unable to complete the degree. What will you do?
49
You see a boy pushing another child into a swimming pool. What will you do?
50
While playing a match you twist your ankle badly. What will you do?
51
You see a car driver beating an auto driver after an accident. What will you do?
52
Your sister’s wedding day arrives but your father is stuck abroad. What will you do?
53
Your scooter hits a truck and you are badly injured. What will you do?
54
While hunting you and your brother lose your way in the jungle at night. What will you do?
55
During an argument your friend punches you. What will you do?
56
Two senior officers give you conflicting orders. What will you do?
57
You have a final exam and a job interview on the same day. What will you do?
58
People usually do not listen to your arguments. What will you do?
59
A gardener beats a boy who stole mangoes during picnic. What will you do?
60
You go to cinema and find the show house-full. What will you do?
61
You planned a picnic with friends but your father refuses permission and friends suggest lying about combined studies. What will you do?
62
A woman suffering from cancer needs 1 million rupees and her husband is your friend with no resources. What will you do?
63
A senior in university used to tease you and later becomes your assistant manager. How will you treat him?
64
Deputy President at ISSB tells you to remove clothes as a condition for selection. What will be your reply?
65
You reached office late and your boss insults you loudly. What will you do?
66
While rushing to hospital you hit a boy with your car and he dies on the spot and nobody saw the accident. What will you do?
67
A student must travel 20 km for entrance test but stepmother refuses bus fare. What should he do?
68
A female psychologist at ISSB attracts you and you feel like proposing marriage. What will you do?
69
During football match your team is losing but coach replaces you though you are playing well. What will you do?
70
A beautiful waitress asks for selfie while you are with family. What will you do?
71
Everyone in department received new computer except you. What will you do?
72
Your friend takes pencils daily from library. What will you do?
73
Your friend’s horse becomes uncontrollable in jungle. What will you do?
74
Your friend damages your camera during picnic. What will you do?
75
GTO asks if you attended an ISSB academy. What will you answer?
76
Girl’s parents insult your poor family after marriage proposal. What will you do?
77
You keep scoring zero runs and may lose place in cricket team. What will you do?
78
You were selected in PMA but expelled for misconduct. What will you do?
79
Friends insist you drink beer or they leave you forever. What will you do?
80
You have patrolling duty but your driver has high fever and no replacement is available. What will you do?
81
You must complete an important task but you meet an accident. What will you do?
82
You see a man park a scooter and leave on another bike. What will you do?
83
You find a suitcase under your seat in train. What will you do?
84
You discover your close friend cheated you. What will you do?
85
Rioters burn your house and your little sister is missing. What will you do?
86
You lost contact with old friends after going abroad. What will you do?
87
You accidentally hit a boy with your car and police arrive. What will you tell them?
88
Your teacher constantly ignores you. What will you do?
89
You are not recommended by ISSB in your third attempt. What will you do?
90
Two candidates have equal merit but one is poor and one is rich. Whom will you select?
91
Students tease a woman in train. What will you do?
92
You want to participate in story competition but fear losing. What will you do?
93
Your friend took sleeping pills and drove a car to another city. What will you do?
94
Gas shortage may cause heavy load shedding in winter. What advice will you give your family?
95
During camping a bear suddenly appears near you. What will you do?
96
At a party someone too drunk wants to drive. What will you do?
97
In job interview you do not know the answer of a question. What will you do?
98
At museum someone tries to steal an artifact. What will you do?
99
At restaurant you receive wrong order. What will you do?
100
Someone offers you drugs at a party. What will you do?
101
At a public event you see someone behaving in a racist manner. What will you do?"""

# Extract non-empty lines cleanly for simple collections
def clean_lines(text):
    return [line.strip() for line in text.split('\n') if line.strip() and not re.match(r'^\d+$', line.strip())]

def clean_sct(text):
    # keep only lines that contain '...' or '___'
    lines = []
    for line in text.split('\n'):
        if re.search(r'[\.\_]{3,}', line):
            # Remove digits at the beginning like "1. " or "  2.  "
            clean = re.sub(r'^\s*\d+\.\s*', '', line).strip()
            lines.append(clean)
    return list(set(lines))

data = {
    "essays": clean_lines(essays_text),
    "sct_english": clean_sct(sct_eng_text),
    "sct_urdu": clean_lines(sct_urd_text),
    "pointer_stories": clean_lines(pointer_text),
    "wat": list(set(clean_lines(wat_text))),
    "srt": clean_lines(srts_text),
}

with open(f"{out_dir}/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Parsed successfully!")
