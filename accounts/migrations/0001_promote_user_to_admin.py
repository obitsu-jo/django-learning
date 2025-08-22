from django.db import migrations

def promote_user_to_admin(apps, schema_editor):
    """
    指定したユーザー名のユーザーを取得し、
    is_staff と is_superuser 属性を True に設定する
    """
    User = apps.get_model('auth', 'User')
    
    # ここに、本番サイトで事前に登録したユーザー名を入力
    USERNAME_TO_PROMOTE = 'admin'

    try:
        user_to_promote = User.objects.get(username=USERNAME_TO_PROMOTE)
        user_to_promote.is_staff = True
        user_to_promote.is_superuser = True
        user_to_promote.save()
        print(f"\nUser '{USERNAME_TO_PROMOTE}' has been promoted to admin.")
    except User.DoesNotExist:
        print(f"\nUser '{USERNAME_TO_PROMOTE}' not found.")


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(promote_user_to_admin),
    ]