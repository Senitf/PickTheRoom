from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Room(models.Model):
    id = models.CharField(max_length=100, primary_key=True)    # Expedia 숙박 시설 ID(property_id)
    name = models.CharField(max_length=100)     # 숙소 이름
    phone = models.CharField(max_length=20)     # 전화번호
    category = models.ForeignKey("Category", related_name="category", on_delete=models.PROTECT)
    rank = models.PositiveIntegerField()    # 전체 순위
    


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('room-detail', args=[self.id])


class Address(models.Model):
    id = models.BigAutoField(primary_key=True)
    line_1 = models.CharField(max_length=200)   # 주소 입력줄1
    line_2 = models.CharField(max_length=200)   # 주소 입력줄2
    city = models.CharField(max_length=100)     # 도시 이름
    postal_code = models.CharField(max_length=50) # 우편번호
    room = models.ForeignKey("Room", related_name="address", on_delete=models.CASCADE)


class Rating(models.Model):
    id = models.BigAutoField(primary_key=True)
    count = models.IntegerField()     # 전체 평점 개수
    overall = models.CharField(max_length=5)    # 평균 평점
    location = models.CharField(max_length=5)    # 접근 편리성 평점
    neighborhood = models.CharField(max_length=5)    # 주변 환경 평점
    value = models.CharField(max_length=5)    # 가격 대비 만족도 평점
    amenities = models.CharField(max_length=5)    # 편의 시설 평점
    recommendation_percent =  models.CharField(max_length=5)    # 숙박 시설을 추천한 고객의 비율
    room = models.ForeignKey("Room", related_name="rating", on_delete=models.CASCADE)


class CheckInOut(models.Model):
    id = models.BigAutoField(primary_key=True)
    checkin_begin_time = models.CharField(max_length=10)    # 체크인 시작 시각
    checkin_end_time = models.CharField(max_length=10)      # 체크인 종료 시각
    checkout_time = models.CharField(max_length=10)         # 체크아웃 시각
    room = models.ForeignKey("Room", related_name="checkInOut", on_delete=models.CASCADE)


