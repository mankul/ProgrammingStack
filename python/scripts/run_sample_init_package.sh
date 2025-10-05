current_dir=$(dirname "$0")
current_dir=$(cd "$current_dir" && pwd)
echo "Current directory: $current_dir"
py_dir=$(cd "$current_dir/.." && pwd)
app_dir=$(cd "$py_dir/apps" && pwd)
echo "Apps directory: $app_dir"
package_dir=$(cd "$current_dir/.." && pwd)
export PYTHONPATH=$PYTHONPATH:$package_dir
echo "PYTHONPATH is set to: $PYTHONPATH"
cmd="python3 $app_dir/run_sample_init_package.py"
echo "Running command: $cmd"
$cmd