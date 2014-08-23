#!/bin/bash
set -e

declare -A aliases
aliases=(
    [8u11-8.2.0.1]='latest'
    [8u11-8.2.0.1]='8'
    [8u11-8.2.0.1]='8u11'
    [8u05-8.1.0.6]='8u5'
    [7u65-7.6.0.1]='7'
    [7u65-7.6.0.1]='7u65'
    [7u60-7.5.0.1]='7u60'
    [7u55-7.4.0.5]='7u55'
    [6u53-6.5.0.2]='6'
    [6u53-6.5.0.2]='6u53'
    [6u49-6.4.0.6]='6u49'
    [6u47-6.3.0.3]='6u47'
)

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")"

versions=( */ )
versions=( "${versions[@]%/}" )
url='git://github.com/zulu-openjdk/zulu-openjdk'

echo '# maintainer: AzulSystems <docker-maintainer@azulsystems.com> (@zulu-openjdk)'

for version in "${versions[@]}"; do
	commit="$(git log -1 --format='format:%H' "$version")"
	versionAliases=( $version ${aliases[$version]} )
	
	echo
	for va in "${versionAliases[@]}"; do
		echo "$va: ${url}@${commit} $version"
	done
done
