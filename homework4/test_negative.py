import pytest
import yaml
from sshcheckers import ssh_checkout, ssh_checkout_negative, ssh_getout, upload_files


with open('folders.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


class TestNegative:
    def save_log(self, start_time, name):
        with open(name, 'a') as f:
            f.write(ssh_getout(data["ip"], data["user"], data["pswd"], f"journalctl --since '{start_time}'"))

    def test_deploy(self, start_time):
        res = []
        upload_files(data["ip"], data["user"], data["pswd"], f'tests/{data["pkgname"]}.deb',
                     f'/home/{data["user"]}/{data["pkgname"]}.deb')
        res.append(ssh_checkout(data["ip"], data["user"], data["pswd"],
                                f'echo "{data["pswd"]}" | sudo -S dpkg -i /home/{data["user"]}/{data["pkgname"]}.deb',
                                "Настраивается пакет"))
        res.append(ssh_checkout(data["ip"], data["user"], data["pswd"],
                                f'echo "{data["pswd"]}" | sudo -S dpkg -s {data["pkgname"]}',
                                "Status: install ok installed"))
        self.save_log(start_time, "log_negative.txt")
        assert all(res), "test_deploy FAIL"

    def test_negative1(self, make_folder, clear_folder, make_files, create_bad_archive,
                       start_time):  
        self.save_log(start_time, "log_negative.txt")
        assert ssh_checkout_negative(data["ip"], data["user"], data["pswd"],
                                     f'cd {data["folder_bad"]}; 7z e arx2.{data["type"]} -o{data["folder_ext"]} -y',
                                     "ERRORS")

    def test_negative2(self, make_folder, clear_folder, make_files, create_bad_archive,
                       start_time):  
        self.save_log(start_time, "log_negative.txt")
        assert ssh_checkout_negative(data["ip"], data["user"], data["pswd"],
                                     f'cd {data["folder_bad"]}; 7z t arx2.{data["type"]}', "Is not")


if __name__ == '__main__':
    pytest.main(['-vv'])