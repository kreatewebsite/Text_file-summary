import os
import argparse as arg_parse
from txt_utils import find_and_read_txt_files, single_file
from summarizer import generate_summary

def main(txt_files,output_dir):

    for txt_path, txt_content in txt_files:
        summary = generate_summary(txt_content)

        summary_filename = os.path.basename(txt_path).split(".")[0] + '_summary.comments'
        summary_path = os.path.join(output_dir, summary_filename)

        if os.path.exists(summary_path):
            os.remove(summary_path)

        with open(summary_path, 'w', encoding='utf-8') as summary_file:
            summary_file.write(summary)

        print(f"Summary saved for {txt_path} at {summary_path}")

def get_args():

    parser = arg_parse.ArgumentParser()

    parser.add_argument("-file", type=str, help="Path to a single text file")
    parser.add_argument("-folder", type=str, help="Path to a folder of txt files")
    parser.add_argument("-output", type=str, help="Path where output file will be saved",required=True)

    args, _ = parser.parse_known_args()
    return args

if __name__ == "__main__":
    args = get_args()
    os.makedirs(args.output, exist_ok=True)

    if args.folder:
        txt_files = find_and_read_txt_files(args.folder)
        main(txt_files, args.output)
    else:
        txt_file = single_file(args.file)
        main(txt_file, args.output)
