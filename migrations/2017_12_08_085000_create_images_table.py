from orator.migrations import Migration


class CreateImagesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('images') as table:
            table.increments('id')
            table.string('title').nullable()
            table.text("url")
            table.integer('category_id', unsigned=True)
            table.string('desc').nullable()
            table.timestamps()
            table.foreign('category_id').references('id').on('categories')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('images')
