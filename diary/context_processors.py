def user_context(request):
    """
    全てのテンプレートにユーザー情報を渡すコンテキストプロセッサ
    """
    # ログインしているユーザーのオブジェクトを取得
    user = request.user
    
    # ログインしている場合のみ、'user' というキーでユーザーオブジェクトを辞書に入れて返す
    # これにより、どのテンプレートでも {{ user.username }} のようにアクセスできる
    if user.is_authenticated:
        return {'user': user}
    
    # ログインしていない場合は、空の辞書を返す
    return {}