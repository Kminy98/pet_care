from django.db import models
from users.models import User


class PetOwner(models.Model):
    species_ = (
        ("cat", "고양이"),
        ("dog", "강아지"),
        ("mammal",'포유류'),
        ("birds", "조류"),
        ("reptile", "파충류"),
        ("fish", "어류"),
        ("amphibian", "양서류"),
        ("rodents", "설치류"),
        ("etc", "기타"),
    )
    reservation_status = (
        ("0","미완료"),
        ("1","예약중"),
        ("2","완료"),
    )
    writer=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField("제목",max_length=20)
    content = models.TextField("내용")
    charge = models.IntegerField("요금")
    species = models.CharField("종", max_length=20, choices=species_)
    is_reserved = models.CharField("진행 상태", max_length=20, choices=reservation_status, default="0") # 기본값을 0으로 주겠습니다
    photo = models.ImageField("이미지", blank=True)

    
    def __str__(self):
        return str(self.title)

class OwnerComment(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # pr? = models.ForeignKey(PR?, on_delete=models.CASCADE)
    # updated_at 처리는 어떻게?
    content = models.TextField()

    def __str__(self):
        return str(self.content)
