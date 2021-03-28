# -*- coding: utf-8 -*-
import click
import logging
from helper import load_and_preprocess
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


@click.command()
#@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
@click.argument('city', type=click.STRING)
def main(output_filepath, city):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    all_city_data = load_and_preprocess(city)
    if output_filepath == "default":
        all_city_data.to_csv("../../data/processed/"+city+".csv")
    else:
        all_city_data.to_csv(output_filepath)
        
if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
