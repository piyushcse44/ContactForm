from django.dispatch import receiver
from django.db.models.signals import post_delete,post_save,pre_save
from user.models import Profile,Skill
from django.core.exceptions import ValidationError




@receiver(post_save,sender = Profile)
def profileupdated(sender,instance,created,**kwargs):
    print("gOod")
    print(sender)
    print(instance)
    print(created)
    Skill.objects.create(
        owner = instance,
        name = instance.skills,
        description = instance.bio,

    )

@receiver(pre_save,sender = Skill)
def Dublicate_skill(sender,instance,created=False,**kwargs):
    skill = instance.name
    if created and Skill.objects.filter(owner = instance.owner,name = skill).exists() :
        raise ValidationError("jaa nahi kar raha save kya kar lega")


@receiver(post_delete,sender = Profile)
def Delete_USER(sender,instance,**kwargs):
    user = instance.user
    user.delete() 

    

        







