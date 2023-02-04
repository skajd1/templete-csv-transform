import csv
import os

file = '공실자료.csv'
f = open(file,'r',encoding='UTF-8')
rdr = csv.reader(f)
row = []
rdr_list = list(rdr)

# row_num = int(input("변환할 행 번호를 입력하세요 : ")) - 1
# selected_row = rdr_list[row_num]

# print("✅위치 : ", selected_row[5], " (건물명: ", selected_row[1], ")")
# print("✅금액 : 보증금", selected_row[8].split('/')[0], "월세", selected_row[8].split('/')[1])
# print("✅전용면적 : ",selected_row[9], " ㎡ ")
# print("✅방향 : ", selected_row[13])
# print("✅구조 : ", selected_row[7])
# print("✅입주가능일 : ", selected_row[6])
# print("✅주차대수 : ", selected_row[14], "대")
# print("✅사용승인일 : ", selected_row[15], "\n")

# print(" ----- ")
# print("건물 설명 직접 입력")
# print("\n")
# print("🚀해당 물건이 내가 찾는 조건 대비 2% 부족한 것 같다면, 다른 매물도 많이 구비하고 있으니 부담없이 문의 부탁드려요!\n")
# print(" ----- \n") 

# print("👌전주 원큐 공인중개사 사무소👌")
# print("❤️대표 공인중개사 : 김다빈")
# print("💜소속 공인중개사 : 최동균")
# print("☎️문의 : 010-5561-6821")
# print("🤞빠른 응답을 원하실 시엔 전화 문의가 빨라요🤞")
# print("🏠위치 : 전북 전주시 완산구 효자동3가 1642-5, 202호\n")
# print(" ----- \n")
# print("👌왜 원큐여야 할까요?👌\n🥇전용 양식을 통해 정확한 조건 파악, 원하시는 매물을 빠르게 찾아드려요🥇\n🥈원하시는 조건에 근접할 때까지 매물을 찾아드려요🥈\n🥉사진을 제공받지 않고, 방문하여 직접 찍은 사진을 사용해요🥉")
# f.close()
# os.system('pause')






