#!/usr/bin/env python

import peewee as pw
import click


sqlite_db = pw.SqliteDatabase('url.db', pragmas={
    'journal_mode': 'wal',
    'cache_size': -1024 * 64})


class savedUrl(pw.Model):

    name = pw.TextField()
    url = pw.TextField()
    category = pw.TextField()

    class Meta:
        database = sqlite_db
        db_table = 'urls'


@click.group()
def cli():
    pass


@cli.command(name='add', help="Add new record to base (name url category)")
@click.argument('add_new', nargs=3)
def add_url_to_base(add_new):
    sqlite_db.connect()
    new_record = savedUrl.create(
        name=add_new[0],
        url=add_new[1],
        category=add_new[2])
    new_record.save()
    sqlite_db.close()


@cli.command(name='del', help="Remove record from db(by id)")
@click.argument('id_url')
def delete_url_from_base(id_url):
    query = savedUrl.get(savedUrl.id == id_url)
    query.delete_instance()


@cli.command(name='all', help="Show all records in database")
def show_all():
    query = savedUrl.select()
    for surl in query:
        print(surl.id, ' | ', surl.name, ' | ', surl.url, ' | ', surl.category)


@cli.command(name='show', help="Show records from category")
@click.argument('show_cat')
def show_category(show_cat: str):
    query = savedUrl.select().where(savedUrl.category == show_cat)
    for surl in query:
        print(surl.id, ' | ', surl.name, ' | ', surl.url)


if __name__ == '__main__':
    cli()
