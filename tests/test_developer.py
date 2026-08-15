from app.developer import Developer

def test_developer_name():
    developer = Developer(
        "Hari",
        2,
        ["Python", "React"]
    )

    assert developer.name == "Hari"
    assert developer.experience == 2
    assert developer.skills == ["Python", "React"]
    
def test_is_senior_developer():
    developer = Developer(
        "Hari",
        4,
        ["Python", "React"]
    )

    assert developer.is_senior() is True
    
def test_non_senior_developer():
    developer = Developer(
        "Hari",
        2,
        ["Python", "React"]
    )

    assert developer.is_senior() is False
    
def test_add_skill():
    developer = Developer(
        "Hari",
        2,
        ["Python", "React"]
    )

    developer.add_skill("FastAPI")

    assert "FastAPI" in developer.skills

def test_has_skill():
    developer = Developer(
        "Hari",
        2,
        ["Python", "React"]
    )

    assert developer.has_skill("Python") is True
    assert developer.has_skill("Java") is False