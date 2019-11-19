""" Build file to download data"""
import parlai.core.build_data as build_data
import os

def build(opt):
    # get path to data directory
    dpath = os.path.join(opt['datapath'], 'oblong')
    # define version if any
    version = '0.0.1'

    # check if data had been previously built
    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')

        # make a clean directory if needed
        if build_data.built(dpath):
            # an older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # # download the data.
        # fname = 'mnist.tar.gz'
        # url = 'http://parl.ai/downloads/mnist/' + fname # dataset URL
        # build_data.download(url, dpath, fname)
        #
        # # uncompress it
        # build_data.untar(dpath, fname)

        # mark the data as built
        build_data.mark_done(dpath, version_string=version)