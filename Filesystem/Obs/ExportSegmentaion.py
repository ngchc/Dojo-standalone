##
##
##

import os
import numpy as np
import h5py
import lxml
import lxml.etree
import UpdateDB as s
import PIL
import PIL.Image
import cv2
import png
import DefaultParams

##

# Not yet
def save_tif16(id_data, filename):
    cv2.imwrite(filename, id_data.astype('uint16'))

def save_tif8(id_data, filename):
    cv2.imwrite(filename, id_data.astype('uint8'))

def save_png16(id_data, filename):
    # Use pypng to write zgray as a grayscale PNG.
    with open(filename, 'wb') as f:
        writer = png.Writer(width=id_data.shape[1], height=id_data.shape[0], bitdepth=16, greyscale=True)
        id_data_list = id_data.astype('uint16').tolist()
        writer.write(f, id_data_list)

def save_png8(id_data, filename):
    # Use pypng to write zgray as a grayscale PNG.
    with open(filename, 'wb') as f:
        writer = png.Writer(width=id_data.shape[1], height=id_data.shape[0], bitdepth=8, greyscale=True)
        id_data_list = id_data.astype('uint8').tolist()
        writer.write(f, id_data_list)


def mkdir_safe( dir_to_make ):
    if not os.path.exists( dir_to_make ):
        execute_string = 'mkdir ' + '"' + dir_to_make + '"'
        print execute_string
        print
        os.system( execute_string )

def load_hdf5(file_path, dataset_name):
    hdf5 = h5py.File(file_path, 'r')
    array = hdf5[dataset_name].value
    hdf5.close()
    return array


###
###
def main(UserInfo, export_path, filetype):
    #
    mojo_tile_path          = UserInfo.mojo_tile_images_path
    mojo_tile_volume_file   = UserInfo.mojo_tile_images_volume_file
    input_color_map_file    = UserInfo.mojo_color_map_file
    export_name             = UserInfo.export_images_name

    #
    with open(mojo_tile_volume_file, 'r') as file:
        idTiledVolDesc = lxml.etree.parse(file).getroot()
    num_tiles_x = int(idTiledVolDesc.get('numTilesX'))  # 1
    num_tiles_y = int(idTiledVolDesc.get('numTilesY'))  # 1
    num_tiles_z = int(idTiledVolDesc.get('numTilesZ'))  # 100
    num_pixels_per_tile_x = int(idTiledVolDesc.get('numVoxelsPerTileX'))  # 512
    num_pixels_per_tile_y = int(idTiledVolDesc.get('numVoxelsPerTileY'))  # 512
    num_pixels_original_image_x = int(idTiledVolDesc.get('numVoxelsX'))  # 512
    num_pixels_original_image_y = int(idTiledVolDesc.get('numVoxelsY'))  # 512


    #
    mkdir_safe( export_path )
    #
    tile_index_w = 0
    for tile_index_z in range(num_tiles_z):
        tmp = os.sep + 'w=' + '%08d' % (tile_index_w) + os.sep + 'z=' + '%08d' % (tile_index_z)
        current_tile_path = mojo_tile_path + tmp
        merged_ids = np.zeros( ( num_pixels_original_image_y, num_pixels_original_image_x ), np.uint32 )
        for tile_index_y in range(num_tiles_y):
            for tile_index_x in range(num_tiles_x):

                # Load and merge panels
                tmp = os.sep + 'y=' + '%08d' % (tile_index_y) + ',' + 'x=' + '%08d' % (tile_index_x) + '.tif'
                current_tile_name = current_tile_path + tmp

                # tile_ids = load_hdf5(current_tile_name, 'IdMap')
                tile_image = PIL.Image.open( current_tile_name )

                y = tile_index_y * num_pixels_per_tile_y
                x = tile_index_x * num_pixels_per_tile_x
                merged_ids[  y : y + num_pixels_per_tile_y, x : x + num_pixels_per_tile_x ] = tile_image

        # Save a merged image
        current_frefix = export_path + os.sep + export_name + 'z%08d' % (tile_index_z)
        if filetype in ['png16', 'png8']:
            current_export_name = current_frefix + '.png'
        elif filetype in ['tif16', 'tif8']:
            current_export_name = current_frefix + '.tif'
        else :
            print 'Export Image Filetype Error.'
            return False
        print current_export_name
        #
        if   filetype == 'png16':
            save_png16(merged_ids, current_export_name)
        elif filetype == 'png8':
            save_png8(merged_ids, current_export_name)
        elif filetype == 'tif16':
            save_tif16(merged_ids, current_export_name)
        elif filetype == 'tif8':
            save_tif8(merged_ids, current_export_name)
        else:
            print 'Export Image Filetype Error.'
            return False
    print 'Images were Exported.'

        # save_u8_to_png(merged_ids, current_export_name)


###
###
