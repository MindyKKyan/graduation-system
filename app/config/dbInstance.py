from app.models.admin import Admin

from app.models.base import db
from app.models.uicer import UICer
from app.models.alumni import Alumni
from app.models.companyOffer import CompanyOffer
from app.models.taughtOffer import TaughtOffer
from app.models.researchOffer import ResearchOffer
from app.models.university import University
from app.models.program import Program
from app.models.employmentExperience import EmploymentExperience

def add_instance():
    with db.auto_commit():
        #uicer
        uicer1 = UICer('Zhangliang', 'zhangliang@mail.uic.edu.hk', 3.43, '123456', 1)
        db.session.add(uicer1)

        uicer2 = UICer('Xiaoming', 'xiaoming@mail.uic.edu.hk', 3.21, '222222', 1)
        db.session.add(uicer2)

        uicer3 = UICer('Zhiyin', 'zhiyin@mail.uic.edu.hk', 3.9, '112233', 1)
        db.session.add(uicer3)

        uicer4 = UICer('Xiaohong', 'xiaohong@mail.uic.edu.hk', 3.7, '6662323', 1)
        db.session.add(uicer4)

        uicer5 = UICer('Mindy', 'mindy@mail.uic.edu.hk', 3.64, '1118', 1)
        db.session.add(uicer5)

        uicer6 = UICer('Caitlyn', 'caitlyn@mail.uic.edu.hk', 3.5, '141913', 1)
        db.session.add(uicer6)



        #alumni
        alumni1 = Alumni('Hejing','hejing@mail.uic.edu.hk',3.4,'123456', 2, True)
        db.session.add(alumni1)

        alumni2 = Alumni('Lihua', 'lihua@mail.uic.edu.hk', 3.2, '654321', 2, False)
        db.session.add(alumni2)

        alumni3 = Alumni('Lily', 'lily@mail.uic.edu.hk', 3.6, '159357', 2, False)
        db.session.add(alumni3)

        alumni4 = Alumni('Helen', 'helen@mail.uic.edu.hk', 3.6, '1342422', 2, False)
        db.session.add(alumni4)

        #admin
        admin = Admin('Luca', '1234', 3)
        db.session.add(admin)

        #companyOffer
        companyOffer1 = CompanyOffer("2020-5-13", 3.4, "HR", "Netease", alumni3)
        companyOffer2 = CompanyOffer("2021-6-20", 3.6, "Tester", "Alibaba", alumni2)
        companyOffer3 = CompanyOffer("2022-4-29", 3.8, "Developer", "ByteDance", alumni4)

        db.session.add(companyOffer1)
        db.session.add(companyOffer2)
        db.session.add(companyOffer3)

        # taughtOffer
        taughtOffer1 = TaughtOffer("2020-10-1", 3.64, "Princeton University", "AI Chatbot", uicer5)
        db.session.add(taughtOffer1)
        taughtOffer2 = TaughtOffer("2022-9-28", 3.5, "Hong Kong University", "UI Design", uicer6)
        db.session.add(taughtOffer2)
        taughtOffer3 = TaughtOffer("2023-2-10", 3.64, "Hong Kong University", "Informational Engineering", uicer5)
        db.session.add(taughtOffer3)


        #researchOffer
        researchOffer1 = ResearchOffer("2022-9-15", 3.5, "UIC", "Data Science", "Tang Tian", "ResearchTopic", 2, 1, uicer6)
        db.session.add(researchOffer1)
        researchOffer2 = ResearchOffer("2022-11-29", 3.9, "Harvard University", "Robot", "Jeremy", "ResearchTopic", 1, 1, uicer3)
        db.session.add(researchOffer2)


        # #employmentExperience
        employmentExperience1 = EmploymentExperience("Alibaba", "I love this job.", companyOffer3)
        db.session.add(employmentExperience1)
        employmentExperience2 = EmploymentExperience('Netease', 'This is a nice experience in the Netease.', companyOffer1)
        db.session.add(employmentExperience2)
        employmentExperience3 = EmploymentExperience('Netease', 'The evironment is comfortable.', companyOffer1)
        db.session.add(employmentExperience3)

        #university
        university1 = University("Princeton University", 1)
        university2 = University("Massachusetts Institute of Technology", 2)
        university3 = University("Harvard University", 3)
        university4 = University("University of Oxford", 4)
        university5 = University("Stanford University", 5)
        university6 = University("California Institute of Technology", 6)
        university7 = University("Imperial College London", 6)
        university8 = University("University College London", 8)
        university9 = University("ETH Zurich", 9)
        university10 = University("National University of Singapore", 11)
        university11 = University("Hong Kong University", 21)
        university12 = University("UIC", 264)


        db.session.add(university1)
        db.session.add(university2)
        db.session.add(university3)
        db.session.add(university4)
        db.session.add(university5)
        db.session.add(university6)
        db.session.add(university7)
        db.session.add(university8)
        db.session.add(university9)
        db.session.add(university10)
        db.session.add(university11)
        db.session.add(university12)

        #program
        program1 = Program("AI Translation", [3.5, 3.7], 1, 'NLP, ML, Python', university4)
        db.session.add(program1)

        program2 = Program("Robot", [3.7, 3.9], 2, 'DSA, CG, CV, DS', university3)
        db.session.add(program2)

        program3 = Program("Data Science", [3.6, 3.8], 3, 'Calculus, DM, Statistics, LA', university3)
        db.session.add(program3)

        program4 = Program("Computer Science", [3.8, 3.9], 2, 'DSA, OS, DS, LA, Calculus, CO, SE', university1)
        db.session.add(program4)

        program5 = Program("Informational Engineering", [3.65, 3.8], 5, 'OS, CO, SE, DSA', university11)
        db.session.add(program5)

        program6 = Program("AI Chatbot", [3.55, 3.74], 4, 'NLP, ML, Python', university1)
        db.session.add(program6)

        program7 = Program("UI Design", [3.46, 3.6], 7, 'SE, SDW, LA, Calculus', university12)
        db.session.add(program7)

        program8 = Program("Bioinformatics", [3.8, 4.0], 1, 'ML, DL, CG, DAA', university9)
        db.session.add(program8)

        program9 = Program("UI Design", [3.67, 3.89], 3, 'SE, SDW, LA, DS', university11)
        db.session.add(program9)



    return 'OK'