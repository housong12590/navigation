from orator.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.string('uid').unique().commit('用户ID')
            table.string('pwd').commit('用户密码')
            table.string('name').nullable().commit('用户姓名')
            table.string('email').nullable().unique().commit('用户邮箱')
            table.string('qq').nullable().commit('qq')
            table.string('mobile').nullable().unique().commit('手机号码')
            table.text('avatar').nullable().commit('头像')
            table.string('signature').nullable().commit('签名信息')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
