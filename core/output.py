import sys
import bpy
import os


def export_blender_file(params: dict, output_dir: str):
    filepath = os.path.join(output_dir, params['filename'])
    bpy.ops.wm.save_as_mainfile(filepath=filepath)


def export_gazebo_model(params: dict, output_dir: str):
    print('export gazebo model')


export_formats = {
    'blender_file': export_blender_file,
    'gazebo_model': export_gazebo_model,
}


def export_from_config(cfg: dict, output_dir: str):
    output_configs = cfg['output']

    for output in cfg['output_enabled']:
        if output not in output_configs:
            print(f"Warning: unknown output config '{output}', skipped", file=sys.stderr)
            continue

        output_config = output_configs[output]
        type = output_config['type']

        if type not in export_formats:
            print(f"Warning: unknown type '{type}' for output config '{output}', skipped",
                  file=sys.stderr)
            continue

        export_formats[type](output_config, output_dir)
