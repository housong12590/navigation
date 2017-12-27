from orator.migrations import Migration


class CreateNotesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('notes') as table:
            table.increments('id')
            table.string('name')
            table.string('title')
            table.string('account')
            table.string('password')
            table.string('desc')
            table.string('link')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('notes')
