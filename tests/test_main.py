from opus_cicala.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Opus Cicala" in captured.out
