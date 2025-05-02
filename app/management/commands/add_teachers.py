from django.core.management.base import BaseCommand
from app.models import Teacher

class Command(BaseCommand):
    help = 'Adds sample teachers to the database'

    def handle(self, *args, **kwargs):
        teachers = [
            {
                'name': 'Dr. Mubashar Mushtaq',
                'department': 'Computer Science',
                'email': 'mubasharmushtaq@fccollege.edu.pk',
                'bio': '''Dr. Mubashar Mushtaq currently serves as an Associate Professor and holds the position of Chairperson in the Department of Computer Science at Forman Christian College. With around 20 years of experience in teaching, research, and management at esteemed institutions, he is a seasoned professional.

His primary research focus revolves around Multimedia Networks and the intricate dynamics of Content Delivery within next-generation networks. Apart from his academic endeavors, he possesses a deep-seated passion for exploring new challenges and opportunities within the ever-evolving field of computing.

Education:
• PhD Computer Science, University of Bordeaux 1, France
• MS Computer Science, University of Bordeaux 1, France
• MSc Computer Science, Quaid-i-Azam University, Islamabad, Pakistan''',
                'office': 'S-201',
                'extension': '530'
            },
            {
                'name': 'Dr. Nazim Ashraf',
                'department': 'Computer Science',
                'email': 'nazimashraf@fccollege.edu.pk',
                'bio': '''Dr. Nazim Ashraf is an associate professor at the department of computer science at Forman Christian College. He has a vast experience in research and teaching. His areas of interest are Machine Learning and Computer Vision. He has also worked in Photonics Information Processing Systems Lab, Department of Electrical & Electronic Engineering at University College Cork, Ireland as a post-doc researcher.

Education:
• PhD. Computer Science, University of Central Florida
• MSc. Computer Science, University of Central Florida
• BSc. (Hons.) Computer Science, Lahore University of Management Sciences''',
                'office': 'S-301',
                'extension': '529'
            },
            {
                'name': 'Dr. Sarwan Altaf Abbasi',
                'department': 'Computer Science',
                'email': 'sarwanabbasi@fccollege.edu.pk',
                'bio': '''As of 2023, he has 17 years of teaching and supervisory experience and 2 years of professional industry experience. Prior to FCCU, he worked as Assistant Professor (Computer Science department) at the Institute of Business Management (IoBM) Karachi, where he taught computing and French courses. Dr. Sarwan received his Ph.D. and MS degrees from Université Paris-Saclay.

Education:
• Ph.D. Computer Science (Université de Paris (SUD-XI), France)
• MS Computer Science (Université de Paris (SUD-XI), France)
• MS (IT) (Hamdard University, Karachi)''',
                'office': 'S-426',
                'extension': '535'
            },
            {
                'name': 'Fakhir Shaheen',
                'department': 'Computer Science',
                'email': 'fakhirshaheen@fccollege.edu.pk',
                'bio': '''Game engine architecture, game development, Graphics rendering pipeline, Data structures, Algorithms, Combinatorics

Education:
• MPhil in Theoretical Computer Science, NUCES-FAST
• BSc in Computer Science, NUCES-FAST
• A-levels, Crescent Model School''',
                'office': 'S426E',
                'extension': '625'
            },
            {
                'name': 'Rabranea Bqa',
                'department': 'Computer Science',
                'email': 'rabraneabqa@fccollege.edu.pk',
                'bio': '''Possessing extensive academic experience, she is an Assistant Professor in Computer Science. She served as a faculty member in the Computer Science department at FAST-NUCES (Lahore) from August 2006 to July 2015 and at UMT (Lahore) from October 2017 to January 2019. Since February 2019, she has been affiliated with Forman Christian College. Her research interests encompass Reverse Engineering and Data Visualization.

Education:
• MS (Computer Science), FAST-National University of Computer and Emerging Sciences, Lahore
• BS (Computer Science), FAST-National University of Computer and Emerging Sciences, Lahore''',
                'office': 'S-426 (I)',
                'extension': '628'
            }
        ]

        for teacher_data in teachers:
            Teacher.objects.get_or_create(
                email=teacher_data['email'],
                defaults={
                    'name': teacher_data['name'],
                    'department': teacher_data['department'],
                    'bio': teacher_data['bio'],
                    'office': teacher_data['office'],
                    'extension': teacher_data['extension']
                }
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully added teacher {teacher_data["name"]}')) 