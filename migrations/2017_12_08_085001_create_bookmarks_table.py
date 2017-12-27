from orator.migrations import Migration


class CreateBookmarksTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('bookmarks') as table:
            table.increments('id')
            table.text('url').commit('标签链接')
            table.long_text('icon').nullable().commit('网站图标')
            table.string('name').nullable().commit('标签名字')
            table.string('uid').commit('用户ID')
            table.integer('browse_count').default(0).commit('浏览次数')
            table.integer('category_id', unsigned=True).commit('分类')
            table.timestamps()
            table.foreign('uid').references('uid').on('users')
            table.foreign('category_id').references('id').on('categories')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('bookmarks')
