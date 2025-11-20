from opus_cicalae.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Opus Cicalae" in captured.out
