from orator.migrations import Migration


class CreateCategoriesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('categories') as table:
            table.increments('id')
            table.string('name').commit('名称')
            table.integer('parent_id', unsigned=True).default(0).commit('上级分类ID')
            table.string('desc').nullable().commit('描述')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('categories')
