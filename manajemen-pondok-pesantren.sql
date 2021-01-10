-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 10 Jan 2021 pada 03.50
-- Versi server: 10.4.11-MariaDB
-- Versi PHP: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `manajemen-pondok-pesantren`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `absen_mengaji`
--

CREATE TABLE `absen_mengaji` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `tgl_absen` date NOT NULL,
  `santri_id` bigint(20) UNSIGNED NOT NULL,
  `ustad_id` bigint(20) UNSIGNED NOT NULL,
  `kitab_id` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `absen_mengaji`
--

INSERT INTO `absen_mengaji` (`id`, `tgl_absen`, `santri_id`, `ustad_id`, `kitab_id`, `created_at`, `updated_at`) VALUES
(1, '2021-01-10', 1, 2, 1, NULL, NULL),
(2, '2021-01-10', 2, 1, 3, NULL, NULL),
(3, '2021-01-10', 2, 3, 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `failed_jobs`
--

CREATE TABLE `failed_jobs` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `connection` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `queue` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `payload` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `exception` longtext COLLATE utf8mb4_unicode_ci NOT NULL,
  `failed_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `jadwal`
--

CREATE TABLE `jadwal` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `hari` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `waktu` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `ustad_id` bigint(20) UNSIGNED NOT NULL,
  `kitab_id` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `jadwal`
--

INSERT INTO `jadwal` (`id`, `hari`, `waktu`, `ustad_id`, `kitab_id`, `created_at`, `updated_at`) VALUES
(1, 'senin', 'ba da magrib', 1, 1, NULL, NULL),
(2, 'selasa', 'ba da bagrib', 2, 3, NULL, NULL),
(3, 'rabu', 'ba da bagrib', 1, 3, NULL, NULL),
(4, 'kamis', 'ba da subuh', 3, 2, NULL, NULL),
(5, 'jumat', 'ba da margib', 2, 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `jaga_pos`
--

CREATE TABLE `jaga_pos` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `tgl_piket` date NOT NULL,
  `kamar_id` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `jaga_pos`
--

INSERT INTO `jaga_pos` (`id`, `tgl_piket`, `kamar_id`, `created_at`, `updated_at`) VALUES
(1, '2021-01-10', 3, NULL, NULL),
(2, '2021-01-10', 1, NULL, NULL),
(3, '2021-01-10', 2, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `kamar`
--

CREATE TABLE `kamar` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `jumlah_kasur` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `kamar`
--

INSERT INTO `kamar` (`id`, `jumlah_kasur`, `created_at`, `updated_at`) VALUES
(1, 5, NULL, NULL),
(2, 8, NULL, NULL),
(3, 6, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `kitab`
--

CREATE TABLE `kitab` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `judul` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pengarang` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `penulis` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tahun_terbit` date NOT NULL,
  `nama_penerbit` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `kitab`
--

INSERT INTO `kitab` (`id`, `judul`, `pengarang`, `penulis`, `tahun_terbit`, `nama_penerbit`, `created_at`, `updated_at`) VALUES
(1, 'bidayatul', 'tidak tahu', 'sama', '2020-12-27', 'PT AksaraArab', NULL, NULL),
(2, 'taklim', 'burhnudin', 'burhan', '2021-01-10', 'PT AksaraArab', NULL, NULL),
(3, 'nahwu', 'abdul aswad', 'abdul ali', '1980-12-11', 'PT MekarArab', NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `migrations`
--

CREATE TABLE `migrations` (
  `id` int(10) UNSIGNED NOT NULL,
  `migration` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `migrations`
--

INSERT INTO `migrations` (`id`, `migration`, `batch`) VALUES
(1, '2019_08_19_000000_create_failed_jobs_table', 1),
(2, '2020_10_29_033915_create_kamars_table', 1),
(3, '2020_11_29_033246_create_kitabs_table', 1),
(4, '2020_11_29_033611_create_santris_table', 1),
(5, '2020_11_29_033724_create_ustads_table', 1),
(6, '2020_11_29_033818_create_penguruses_table', 1),
(7, '2020_11_29_033939_create_jaga_pos_table', 1),
(8, '2020_11_29_034043_create_absen_mengajis_table', 1),
(9, '2020_11_29_034116_create_pengumuman_table', 1),
(10, '2020_11_29_034141_create_transaksis_table', 1),
(11, '2020_12_23_021334_create_jadwals_table', 1);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengumuman`
--

CREATE TABLE `pengumuman` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `isi_pengumuman` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `pengurus_id` bigint(20) UNSIGNED NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pengumuman`
--

INSERT INTO `pengumuman` (`id`, `isi_pengumuman`, `pengurus_id`, `created_at`, `updated_at`) VALUES
(1, 'akan diadakan pengajian rutinan malem jumat', 1, NULL, NULL),
(2, 'akan diadakan pengajian rutinan malem jumat', 2, NULL, NULL),
(3, 'santri yang belum bayar spp untuk segera bayar', 2, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengurus`
--

CREATE TABLE `pengurus` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nama` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `alamat` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `no_hp` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `jabatan` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `pengurus`
--

INSERT INTO `pengurus` (`id`, `nama`, `email`, `password`, `alamat`, `no_hp`, `jabatan`, `created_at`, `updated_at`) VALUES
(1, 'duhal', 'duhal@gmail.com', '12345', 'genteng banyuwangi', '083146681324', 'ketua umum', NULL, NULL),
(2, 'faiz', 'faiz@gmail.com', '12345', 'sumbersari jember', '083146681324', 'bendahara', NULL, NULL),
(3, 'said', 'said@gmail.com', '12345', 'kencong jember', '083146681324', 'sekretaris', NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `santri`
--

CREATE TABLE `santri` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nama` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `alamat` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `no_hp` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `perguruan_tinggi` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `prodi` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `kamar_id` bigint(20) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `santri`
--

INSERT INTO `santri` (`id`, `nama`, `email`, `password`, `alamat`, `no_hp`, `perguruan_tinggi`, `prodi`, `kamar_id`, `created_at`, `updated_at`) VALUES
(1, 'rifky', 'rifky@gmail.com', '12345', 'sempu banyuwangi', '082140091325', 'universitas jember', 'informatika', 1, NULL, NULL),
(2, 'marha', 'martha@gmail.com', '12345', 'sempu banyuwangi', '082140091325', 'uin jember', 'teknik informatika', 2, NULL, NULL),
(3, 'bima', 'bimaa@gmail.com', '12345', 'tulungagung', '082140091456', 'poltek jember', 'sistem informasi', 3, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi`
--

CREATE TABLE `transaksi` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `tgl_pembayaran` date NOT NULL,
  `nominal` decimal(10,2) NOT NULL,
  `jenis_transaksi` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `santri_id` bigint(20) UNSIGNED DEFAULT NULL,
  `pengurus_id` bigint(20) UNSIGNED DEFAULT NULL,
  `ustad_id` bigint(20) UNSIGNED DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `transaksi`
--

INSERT INTO `transaksi` (`id`, `tgl_pembayaran`, `nominal`, `jenis_transaksi`, `santri_id`, `pengurus_id`, `ustad_id`, `created_at`, `updated_at`) VALUES
(1, '2021-01-10', '2000.00', 'spp', 1, NULL, NULL, NULL, NULL),
(2, '2021-01-10', '50000.00', 'listrik', NULL, 2, NULL, NULL, NULL),
(5, '2021-01-10', '100000.00', 'spp', 1, 2, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Struktur dari tabel `ustad`
--

CREATE TABLE `ustad` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `nama` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `alamat` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `no_hp` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data untuk tabel `ustad`
--

INSERT INTO `ustad` (`id`, `nama`, `email`, `password`, `alamat`, `no_hp`, `created_at`, `updated_at`) VALUES
(1, 'suparman', 'suparman@gmail.com', '12345', 'Jember', '082140091358', NULL, NULL),
(2, 'marwan', 'marwan@gmail.com', '12345', 'Jember', '082140091358', NULL, NULL),
(3, 'mirwan', 'mirwan@gmail.com', '12345', 'Jember', '082140091358', NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `absen_mengaji`
--
ALTER TABLE `absen_mengaji`
  ADD PRIMARY KEY (`id`),
  ADD KEY `absen_mengaji_santri_id_foreign` (`santri_id`),
  ADD KEY `absen_mengaji_ustad_id_foreign` (`ustad_id`),
  ADD KEY `absen_mengaji_kitab_id_foreign` (`kitab_id`);

--
-- Indeks untuk tabel `failed_jobs`
--
ALTER TABLE `failed_jobs`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `jadwal`
--
ALTER TABLE `jadwal`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jadwal_ustad_id_foreign` (`ustad_id`),
  ADD KEY `jadwal_kitab_id_foreign` (`kitab_id`);

--
-- Indeks untuk tabel `jaga_pos`
--
ALTER TABLE `jaga_pos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jaga_pos_kamar_id_foreign` (`kamar_id`);

--
-- Indeks untuk tabel `kamar`
--
ALTER TABLE `kamar`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `kitab`
--
ALTER TABLE `kitab`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `migrations`
--
ALTER TABLE `migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `pengumuman`
--
ALTER TABLE `pengumuman`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pengumuman_pengurus_id_foreign` (`pengurus_id`);

--
-- Indeks untuk tabel `pengurus`
--
ALTER TABLE `pengurus`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `santri`
--
ALTER TABLE `santri`
  ADD PRIMARY KEY (`id`),
  ADD KEY `santri_kamar_id_foreign` (`kamar_id`);

--
-- Indeks untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `transaksi_santri_id_foreign` (`santri_id`),
  ADD KEY `transaksi_pengurus_id_foreign` (`pengurus_id`),
  ADD KEY `transaksi_ustad_id_foreign` (`ustad_id`);

--
-- Indeks untuk tabel `ustad`
--
ALTER TABLE `ustad`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `absen_mengaji`
--
ALTER TABLE `absen_mengaji`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `failed_jobs`
--
ALTER TABLE `failed_jobs`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT untuk tabel `jadwal`
--
ALTER TABLE `jadwal`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `jaga_pos`
--
ALTER TABLE `jaga_pos`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `kamar`
--
ALTER TABLE `kamar`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `kitab`
--
ALTER TABLE `kitab`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `migrations`
--
ALTER TABLE `migrations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT untuk tabel `pengumuman`
--
ALTER TABLE `pengumuman`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `pengurus`
--
ALTER TABLE `pengurus`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `santri`
--
ALTER TABLE `santri`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT untuk tabel `ustad`
--
ALTER TABLE `ustad`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `absen_mengaji`
--
ALTER TABLE `absen_mengaji`
  ADD CONSTRAINT `absen_mengaji_kitab_id_foreign` FOREIGN KEY (`kitab_id`) REFERENCES `kitab` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `absen_mengaji_santri_id_foreign` FOREIGN KEY (`santri_id`) REFERENCES `santri` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `absen_mengaji_ustad_id_foreign` FOREIGN KEY (`ustad_id`) REFERENCES `ustad` (`id`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `jadwal`
--
ALTER TABLE `jadwal`
  ADD CONSTRAINT `jadwal_kitab_id_foreign` FOREIGN KEY (`kitab_id`) REFERENCES `kitab` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `jadwal_ustad_id_foreign` FOREIGN KEY (`ustad_id`) REFERENCES `ustad` (`id`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `jaga_pos`
--
ALTER TABLE `jaga_pos`
  ADD CONSTRAINT `jaga_pos_kamar_id_foreign` FOREIGN KEY (`kamar_id`) REFERENCES `kamar` (`id`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `pengumuman`
--
ALTER TABLE `pengumuman`
  ADD CONSTRAINT `pengumuman_pengurus_id_foreign` FOREIGN KEY (`pengurus_id`) REFERENCES `pengurus` (`id`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `santri`
--
ALTER TABLE `santri`
  ADD CONSTRAINT `santri_kamar_id_foreign` FOREIGN KEY (`kamar_id`) REFERENCES `kamar` (`id`) ON DELETE CASCADE;

--
-- Ketidakleluasaan untuk tabel `transaksi`
--
ALTER TABLE `transaksi`
  ADD CONSTRAINT `transaksi_pengurus_id_foreign` FOREIGN KEY (`pengurus_id`) REFERENCES `pengurus` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `transaksi_santri_id_foreign` FOREIGN KEY (`santri_id`) REFERENCES `santri` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `transaksi_ustad_id_foreign` FOREIGN KEY (`ustad_id`) REFERENCES `ustad` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
