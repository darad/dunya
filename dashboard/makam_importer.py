# Copyright 2013,2014 Music Technology Group - Universitat Pompeu Fabra
# 
# This file is part of Dunya
# 
# Dunya is free software: you can redistribute it and/or modify it under the
# terms of the GNU Affero General Public License as published by the Free Software
# Foundation (FSF), either version 3 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see http://www.gnu.org/licenses/

import django.utils.timezone

from dashboard.log import logger
from dashboard import release_importer

import makam
import data

class MakamReleaseImporter(release_importer.ReleaseImporter):
    _ArtistClass = makam.models.Artist
    _ComposerClass = makam.models.Composer
    _ReleaseClass = makam.models.Release
    _RecordingClass = makam.models.Recording
    _InstrumentClass = makam.models.Instrument
