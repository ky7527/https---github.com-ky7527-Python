#버스의 정원
# 우리 학교 공학기술교육혁신센터에서는 메카트로닉스 업체를 탐방하기로 하였습니다.
# 메카트로닉스는 우리 센터에서 특성화 영역으로 설정하여 창의적 인재를 양성하고 있기 때문입니다.
# 탐방에 참여하는 전체 인원은 50명이고, 타고 갈 버스는 큰 버스와 작은 버스 2대입니다.
# 버스 2대의 전체 정원은 50명으로서 탐방에 참여하는 인원과 같고, 큰 버스는 작은 버스보다 정원이 10명 많습니다.
# 큰 버스와 작은 버스의 정원은 각각 몇 명일까요?
# 답은 큰 버스는 30명, 작은 버스는 20명입니다.

# 탐방에 참여하는 전체 인원과 큰 버스의 정원이 작은 버스의 정원보다 몇 명이 더 많은지 입력받아서,
# 큰 버스의 정원과 작은 버스의 정원을 구하여 보세요.
# 탐방에 참여하는 전체 인원과 버스 전체의 정원은 같습니다.

# Input
# 첫째 줄에 탐방에 참여하는 전체 인원,
# 둘째 줄에 큰 버스의 정원이 작은 버스의 정원보다 몇 명이 더 많은지 입력됩니다.

# Output
# 첫째 줄에 큰 버스의 정원,
# 둘째 줄에 작은 버스의 정원을 출력합니다.

t = int(input())
a = int(input())

bus1 = (t/2) + (a/2)
bus2 = (t/2) - (a/2)

print(int(bus1))
print(int(bus2))